from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import include, path
from users import views as user_views
from django.conf import settings
from django.contrib import admin
from blog import views
from users.views import logout_view, profile
# from comptes.views import login_user, logout_user, signup, profile
# from store.views import ajouter_au_panier, delete_panier, panier, produit_detail, store

app_name = 'blog'

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # Accueil, about et contact
    path('', views.index, name='blog'),
    path('about/', views.about, name='blog_about'),
    path('contact/', views.contact, name='blog_contact'),

    # Blog
    path('list_article/', views.list_article, name='list_article'),
    path('categorie/<slug:categorie>/', views.list_article, name='categorie_article_list'),
    path('tag/<slug:tag_slug>/', views.list_article, name='tag_by_article_list'),
    path('article/<str:slug>/', views.detail_article, name='detail_article'),
    path('categorie/<slug:categorie>/', views.detail_article, name='categorie_article_list'),
    path('search/', views.article_search, name='article_search'),
    path('ajouter_article/', views.ajouter_article, name='ajouter_article'),
    path('modifier_article/<int:article_id>/', views.modifier_article, name='modifier_article'),
    path('article/<int:pk>/supprimer', views.supprimer_article, name='supprimer_article'),

    # Comptes Users
    path('inscription/', user_views.inscription, name='inscription'),
    path('connexion/',
        auth_views.LoginView.as_view(
            template_name='users/pages/connexion.html'
        ), name='connexion'),
    path('reset_mot2passe/',
        auth_views.PasswordResetView.as_view(
            template_name='users/mot2passe_users/reset_mot2passe.html'
        ), name='reset_mot2passe'),
    path('reset_mot2passe/valider/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/mot2passe_users/reset_mot2passe_valider.html'
        ), name='password_reset_done'),
    path('reset_mot2passe_confirmation/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/mot2passe_users/reset_mot2passe_confirmation.html'
        ), name='password_reset_confirm'),
    path('reset_mot2passe_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/mot2passe_users/reset_mot2passe_complete.html'
        ), name='password_reset_complete'),
    path('logout/', logout_view, name='logout'),
    # path('login/', login_user, name='login'),
    # path('signup/', signup, name='signup'),
    # path('logout/', logout_user, name='logout'),
    path('profile/', user_views.profile, name='profile'),

    # path('store/', store, name='store'),
    # path('produit/<str:slug>/', produit_detail, name='produit'),
    # path('produit/<str:slug>/ajouter-au-panier/', ajouter_au_panier, name='ajouter-au-panier'),
    # path('panier/', panier, name='panier'),
    # path('panier/delete/', delete_panier, name='delete-panier'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns