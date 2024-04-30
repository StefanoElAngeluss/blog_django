from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a bien été crée {username}. Vous pouvez maintenant vous connecter.')
            return redirect('blog')
    else:
        form = UserRegisterForm()
    return render(request, 'users/pages/inscription.html', {'form': form})

def logout_view(request):
    messages.success(request, f'Vous avez bien été déconnecté et vous pouvez vous reconnecter à nouveau.')
    logout(request)
    return redirect('blog')  # Rediriger vers la page de connexion après déconnexion

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if 'delete_image' in request.POST:  # Si le bouton de suppression d'image est cliqué
            profile = request.user.profile
            if profile.image:  # Vérifie si l'utilisateur a une image de profil
                profile.image.delete()  # Supprime l'image de profil
                profile.save()  # Enregistre le profil
                messages.success(request, 'Image de profil supprimée avec succès!')
                return redirect('users:profile')  # Redirige vers la page de profil

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre profil a bien été mis à jour.')
            return redirect('users:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/pages/profile.html', context)
