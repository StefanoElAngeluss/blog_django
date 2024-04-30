from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings
from blog import views
# from store.views import ajouter_au_panier, delete_panier, panier, produit_detail, store

app_name = 'blog'

urlpatterns = [
    # Blog
    path('list_article/', views.list_article, name='list_article'),
    path('categorie/<slug:categorie>/', views.list_article, name='categorie_article_list'),
    path('tag/<slug:tag_slug>/', views.list_article, name='tag_by_article_list'),
    path('article/<str:slug>/', views.detail_article, name='detail_article'),
    path('categorie/<slug:categorie>/', views.detail_article, name='categorie_article_list'),
    path('search/', views.article_search, name='article_search'),
    path('ajouter_article/', views.ajouter_article, name='ajouter_article'),
    path('modifier_article/<int:article_id>/', views.modifier_article, name='modifier_article'),
    path('article/<int:pk>/supprimer', views.supprimer_article, name='supprimer_article'),

    # path('store/', store, name='store'),
    # path('produit/<str:slug>/', produit_detail, name='produit'),
    # path('produit/<str:slug>/ajouter-au-panier/', ajouter_au_panier, name='ajouter-au-panier'),
    # path('panier/', panier, name='panier'),
    # path('panier/delete/', delete_panier, name='delete-panier'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)