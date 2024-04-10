from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from blog import views
from blog.views import detail_article, list_article
from comptes.views import login_user, logout_user, signup
from store.views import ajouter_au_panier, delete_panier, panier, produit_detail, store

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='blog'),
    path('list_article/', list_article, name='list_article'),
    path('categorie/<slug:categorie>/', list_article, name='categorie_article_list'),
    path('article/<str:slug>/', detail_article, name='detail_article'),
    path('categorie/<slug:categorie>/', detail_article, name='categorie_article_list'),
    path('search/', views.article_search, name='article_search'),
    path('ajouter_article/', views.ajouter_article, name='ajouter_article'),
    path('modifier_article/<int:article_id>/', views.modifier_article, name='modifier_article'),
    path('store/', store, name='store'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('produit/<str:slug>/', produit_detail, name='produit'),
    path('produit/<str:slug>/ajouter-au-panier/', ajouter_au_panier, name='ajouter-au-panier'),
    path('panier/', panier, name='panier'),
    path('panier/delete/', delete_panier, name='delete-panier'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns