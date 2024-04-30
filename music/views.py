from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from music.models import Musique
from music.forms import MusiqueForm

def liste_musique(request):
    musiques = Musique.objects.all()
    return render(request, 'liste_musique.html', {'musiques': musiques})

@login_required
def ajouter_musique(request):
    if request.method == 'POST':
        form = MusiqueForm(request.POST, request.FILES)
        if form.is_valid():
            musique = form.save(commit=False)
            musique.artiste = request.user
            musique.save()
            return redirect('music:liste_musique')
    else:
        form = MusiqueForm()
    return render(request, 'ajouter_musique.html', {'form': form})

def supprimer_musique(request, musique_id):
    musique = Musique.objects.get(id=musique_id)
    musique.delete()
    return redirect('music:liste_musique')