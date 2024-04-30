from django.contrib.auth.models import User
from django.db import models
import os

class Musique(models.Model):
    titre = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='sons/')
    artiste = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

    def delete(self, *args, **kwargs):
        # Supprimer le fichier audio du système de fichiers
        if os.path.isfile(self.fichier.path):
            os.remove(self.fichier.path)
        # Supprimer l'objet Musique
        super().delete(*args, **kwargs)