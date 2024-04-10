from datetime import datetime, timezone
from django.db import models
from django.urls import reverse
from main.settings import AUTH_USER_MODEL

fuseau_utc = timezone.utc

class Produit(models.Model):
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    prix = models.FloatField(default=0.0)
    quantite = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='produits/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - ({self.prix}€) - ({self.quantite} en stock)"

    def get_absolute_url(self):
        return reverse("produit", kwargs={"slug": self.slug})

class Commande(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    client = models.BooleanField(default=False)
    client_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.produit.nom} ({self.quantite})"

class Panier(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    commandes = models.ManyToManyField(Commande)

    def __str__(self):
        return self.utilisateur.username

    def delete(self, *args, **kwargs):
        for commande in self.commandes.all():
            commande.client = True
            commande.client_date = datetime.now(fuseau_utc)
            commande.save()

        self.commandes.clear()
        super().delete(*args, **kwargs)
