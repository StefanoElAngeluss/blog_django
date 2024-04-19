# from django.contrib.auth import get_user_model, authenticate, login, logout
# from django.shortcuts import render, redirect
# from django.contrib import messages

# from blog.models import Article, Commentaire

# User = get_user_model()

# def profile(request):
#     user = request.user
#     article_count = Article.objects.filter(auteur=user).count()
#     commentaire_count = Commentaire.objects.filter(auteur=user).count()
#     return render(request, 'comptes/profile.html', {'article_count': article_count, 'commentaire_count': commentaire_count})

# def signup(request):
#     if request.method == "POST":
#         # Traiter le formulaire de l'utilisateur
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         email = request.POST.get("email")
#         user = User.objects.create_user(username=username, email=email, password=password) # type: ignore
#         user.save()
#         if user:
#             login(request, user)
#             messages.success(request, f'Votre compte a bien été crée {username}. Vous pouvez maintenant vous connecter.')
#             return redirect('blog')

#     return render(request, 'comptes/signup.html')

# def login_user(request):
#     if request.method == "POST":
#         # Connexion utilisateur
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('blog')

#     return render(request, 'comptes/login.html')

# def logout_user(request):
#     logout(request)
#     return redirect('blog')
