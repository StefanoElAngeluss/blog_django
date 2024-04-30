from django import forms
from music.models import Musique

class MusiqueForm(forms.ModelForm):
    class Meta:
        model = Musique
        fields = ['titre', 'fichier']
