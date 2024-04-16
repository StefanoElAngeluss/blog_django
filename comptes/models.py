from django.contrib.auth.models import AbstractUser
from django.db import models

class Acheteur(AbstractUser, models.Model):
    pass
    image = models.ImageField(blank=True, null=True, upload_to='images/profile/')

    def __str__(self):
        return f'{self.username}'