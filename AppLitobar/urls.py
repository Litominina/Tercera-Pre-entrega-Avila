from django.contrib import admin
from django.urls import path
from AppLitobar import views


urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("cita/", views.cita, name="cita"),
    path("apoderados/", views.apoderado, name="apoderado"),
    path("mascotas/", views.mascotas, name="mascotas"),
    
]