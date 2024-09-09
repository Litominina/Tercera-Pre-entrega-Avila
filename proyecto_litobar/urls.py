from django.contrib import admin
from django.urls import path, include
from proyecto_litobar.views import saludo, otra_vista, dia_de_hoy, muestra_nombre, probando_template, agendar_cita
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("AppLitobar.urls")),
    path("saludo/", saludo),
    path("otra_vista/", otra_vista),
    path("dia/", dia_de_hoy),
    path("nombre/<nombre>/", muestra_nombre),
    path("plantillas/", probando_template),
    path("agendar_cita/<fech>/<mot>/<vet>/", agendar_cita),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
