from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Votre compte a bien été crée {username}. Vous pouvez maintenant vous connecter.')
            return redirect('connexion')
    else:
        form = UserRegisterForm()
    return render(request, 'users/pages/inscription.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/pages/profile.html')