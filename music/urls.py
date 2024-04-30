from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from music import views

app_name = 'music'

urlpatterns = [
    path('', views.liste_musique, name='liste_musique'),
    path('ajouter-musique/', views.ajouter_musique, name='ajouter_musique'),
    path('supprimer-musique/<int:musique_id>/', views.supprimer_musique, name='supprimer_musique'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)