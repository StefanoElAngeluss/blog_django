from django.conf.urls.static import static
from django.urls import path, include
from store.views import store

from django.conf import settings

app_name = 'store'

urlpatterns = [
    path('', store, name='store'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns