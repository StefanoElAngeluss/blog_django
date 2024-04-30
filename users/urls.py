from django.contrib.auth import views as auth_views
from users.views import logout_view
from django.conf.urls.static import static
from users import views as user_views
from django.urls import path
from django.conf import settings

app_name = 'users'

urlpatterns = [
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
    path('profile/', user_views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)