from django.shortcuts import render
from django.http import HttpResponse
from .models import Cita

# Create your views here.

def inicio(req):
    return render(req, "AppLitobar/index.html")

def cita(req):
    return render(req, "AppLitobar/cita.html")

def apoderado(req):
    return render(req, "AppLitobar/apoderados.html")

def mascotas(req):
    return render(req, "AppLitobar/mascotas.html")
