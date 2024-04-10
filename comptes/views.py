from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

User = get_user_model()

def signup(request):
    if request.method == "POST":
        # Traiter le formulaire de l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        if user:
            login(request, user)
            return redirect('blog')

    return render(request, 'comptes/signup.html')

def login_user(request):
    if request.method == "POST":
        # Connexion utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog')

    return render(request, 'comptes/login.html')

def logout_user(request):
    logout(request)
    return redirect('blog')