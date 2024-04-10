from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# PublicationManager
class PublicationManager(models.Manager):
    def get_queryset(self):
        return super(PublicationManager, self).get_queryset().filter(status='publier')

# Catégories
class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom

# Articles
class Article(models.Model):
    STATUS_CHOICES = (
        ('publier', 'Publié'),
        ('brouillon', 'Brouillon'),
    )
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    contenu = RichTextField()
    status = models.CharField(choices=STATUS_CHOICES,
                              default='brouillon',
                              max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="posted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publication = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # The default manager.
    publier = PublicationManager()  # Publier manager for articles.
    tags = TaggableManager() # Tag manager for articles

    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Article, self).save(*args, **kwargs)

# Commentaires
class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="commentaires")
    email = models.EmailField(max_length=200)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="blog_commentaire_auteur")
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return self.article.titre
