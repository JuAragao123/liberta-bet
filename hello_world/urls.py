from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from liberta.views import (
    login_view,
    pagina_inicial_view,
    diferenca_view,
    depoimentos_view,
    apoio_view,
    chat_view,
    progresso_view
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path('', pagina_inicial_view, name='pagina_inicial'),
    path('login/', login_view, name='login'),
    path('diferencas/', diferenca_view, name='diferencas'),
    path('depoimentos/', depoimentos_view, name='depoimentos'),
    path('apoio/', apoio_view, name='apoio'),
    path('chat/', chat_view, name='chat'),
    path('progresso/', progresso_view, name='progresso'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
