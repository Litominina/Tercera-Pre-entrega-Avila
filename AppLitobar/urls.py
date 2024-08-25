from django.contrib import admin
from django.urls import path
from AppLitobar import views


urlpatterns = [
    path("inicio/", views.busqueda_mascota, name="inicio"),
    path("cita/", views.cita_formulario, name="cita"),  # Esta URL ahora apunta a la vista 'cita_formulario'
    path("apoderados/", views.apoderados_formulario, name="apoderado"),
    path("mascotas/", views.mascotas_formulario, name="mascotas"),
#    path('busquedamascota/', views.busqueda_mascota, name='BusquedaMascota'),
    path('buscar/', views.buscar, name="buscar"),
]