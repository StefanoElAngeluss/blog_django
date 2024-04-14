from typing import List
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from blog.models import Article, Commentaire, Categorie

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'status', 'categorie', 'tags', 'date_creation', 'publication')
    list_filter = ('auteur', 'status', 'publication')
    list_editable: List[str] = ['tags', 'status', 'categorie']
    ordering = ('auteur', 'status', 'publication')
    prepopulated_fields = {'slug': ('titre',)}
    search_fields = ('titre', 'contenu', 'status')

    def date_creation(self, obj):
            return obj.created_at

    def tags(self, obj):
        return ", ".join([tag.nom for tag in obj.tags.all()])
    tags.short_description = 'Tags'

    date_creation.short_description = 'Date de création'

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'email', 'created_at')
    list_filter = ('auteur', 'created_at')

class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nom',)}


class ArticleForm(forms.ModelForm):
    contenu = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article
        fields = ('titre', 'categorie', 'contenu', 'image', 'auteur')

admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie, CategorieAdmin)