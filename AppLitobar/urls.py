from django.contrib import admin
from django.urls import path
from AppLitobar import views


urlpatterns = [
    path("inicio/", views.inicio),
    path("cita/", views.cita),
    path("apoderados/", views.apoderado),
    path("mascotas/", views.mascotas),
    
]