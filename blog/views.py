from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator
)
from django.contrib.postgres.search import (
    # SearchVector,
    # SearchQuery,
    # SearchRank,
    TrigramSimilarity,
)

from taggit.models import Tag
from blog.models import Article, Categorie, Commentaire
from blog.forms import CommentaireForm, SearchArticle, ArticleForm
from django.contrib import messages

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def list_article(request, categorie=None, tag_slug=None):
    articles = Article.publier.all()
    categories = Categorie.objects.all()
    tag = None
    if categorie:
        categorie = get_object_or_404(Categorie, slug=categorie)
        articles = articles.filter(categorie=categorie).order_by('created_at')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags__in=[tag]).order_by('created_at')
    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'articles': articles,
        'page': page,
        'categories': categories,
        'tag': tag,
    }

    return render(request, 'blog/article/list.html', context)

def detail_article(request, slug, categorie=None):
    article = get_object_or_404(Article, slug=slug)
    categories = Categorie.objects.all()
    if categorie:
        categorie = get_object_or_404(Categorie, slug=categorie)
        article = Article.objects.filter(categorie=categorie).order_by('created_at')
    comments = Commentaire.objects.filter(article=article)
    new_commentaire = None
    if request.method == 'POST':
        comment_form = CommentaireForm(data=request.POST)
        if comment_form.is_valid():
            new_commentaire = comment_form.save(commit=False)
            new_commentaire.article = article
            new_commentaire.auteur = request.user
            new_commentaire.email = request.user.email
            new_commentaire.save()
    else:
        comment_form = CommentaireForm()
    return render(request, 'blog/article/detail.html', {
                    'article': article,
                    'comments': comments,
                    'new_commentaire': new_commentaire,
                    'comment_form': comment_form,
                    'categories': categories,
                    })

def article_search(request):
    query = None
    results = []
    search_form = SearchArticle()
    if 'query' in request.GET:
        search_form = SearchArticle(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            # vector_search = SearchVector('titre', weight='A') + SearchVector('contenu', weight='B')
            # query_search = SearchQuery(query)
            # results = Article.publier.annotate(
            #     search=vector_search, rank=SearchRank(vector_search, query_search)
            #     ).filter(rank__gte=0.3).order_by('-rank')
            results = Article.publier.annotate(
                                    similarity=TrigramSimilarity('titre', query),
                                    ).filter(similarity__gte=0.1).order_by('-similarity')
    return render(request, 'blog/article/search.html',
                {
                    'search_form': search_form,
                    'query': query,
                    'results': results,
                })

def ajouter_article(request):
    if request.method=='POST':
        form = ArticleForm(request.POST or None, request.FILES or None, user=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.auteur = request.user
            obj.save()
            messages.success(request, f'Votre article {obj.titre} a bien été crée et sera publiée après validation par l\'administrateur.')
            return redirect('list_article')
    else:
        form = ArticleForm()
    return render(request, 'blog/article/ajoutArticle.html', {'form': form})

def modifier_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            return redirect('list_article')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article/modifierArticle.html', {'form': form})