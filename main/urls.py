from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from main import views

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),
    path('', views.index, name='blog'),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('about/', views.about, name='blog_about'),
    path('contact/', views.contact, name='blog_contact'),
    path('music/', include('music.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)