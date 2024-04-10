from django import forms
# from ckeditor.widgets import CKEditorWidget
from blog.models import Article, Categorie, Commentaire


class ArticleForm(forms.ModelForm):
    # contenu = forms.CharField(widget=CKEditorWidget())
    # categories = Categorie.objects.all()
    class Meta:
        model = Article
        fields = ('titre', 'auteur', 'contenu', 'categorie', 'image')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Titre'})
        self.fields['auteur'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Auteur'})
        self.fields['contenu'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contenu'})
        self.fields['categorie'].widget.attrs.update({'class': 'form-control custom-select'})  # Utilisation d'un select pour les catégories
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})  # Ajout de la classe pour le champ image
        self.fields['categorie'].queryset = Categorie.objects.all()  # Charger toutes les catégories disponibles dans le champ select

class CommentaireForm(forms.ModelForm):
    contenu = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Commentaire
        fields = ['contenu']

class SearchArticle(forms.Form):
    query = forms.CharField(max_length=200)

    class Meta:
        fields = ['query']
