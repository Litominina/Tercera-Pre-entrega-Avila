from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppLitobar.models import Cita, Mascota, Apoderado
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(req):
    return render(req, "AppLitobar/daddy.html")


def about(req):
    return render(req, "AppLitobar/acerca_de_mi.html")

def nada(req):
    return render(req, "AppLitobar/en_blanco.html")

@login_required
def cita(req):
    return render(req, "AppLitobar/cita.html")

@login_required
def apoderado(req):
    return render(req, "AppLitobar/apoderados.html")

@login_required
def mascotas(req):
    return render(req, "AppLitobar/mascotas.html")

@login_required
def cita_formulario(req):
    if req.method == 'POST':
        cita = Cita(
            fecha=req.POST['cita'],
            motivo=req.POST['motivo'],
            veterinario=req.POST['veterinario']
        )
        cita.save()

        return redirect('inicio')

    return render(req, "AppLitobar/cita.html")


@login_required
def mascotas_formulario(req):
    if req.method == 'POST':
        cita = Mascota(
            nombre_mascota=req.POST['nombre_mascota'],
            tipo=req.POST['tipo'],
            raza=req.POST['raza'],
            edad=req.POST['edad'],
        )
        cita.save()

        return redirect('inicio')

    return render(req, "AppLitobar/mascotas.html")

@login_required
def apoderados_formulario(req):
    if req.method == 'POST':
        cita = Apoderado(
            nombre_apoderado=req.POST['nombre_apoderado'],
            apellido=req.POST['apellido'],
            email=req.POST['email'],
            telefono=req.POST['telefono'],
        )
        cita.save()

        return redirect('inicio')

    return render(req, "AppLitobar/apoderados.html")


@login_required
def busqueda_mascota(request):
    return render(request, "AppLitobar/mascotas.html")


@login_required
def buscar(request):

    if request.GET["nombre_mascota"]:

        nombre_mascota = request.GET['nombre_mascota']

        mascotas = Mascota.objects.filter(nombre_mascota__icontains=nombre_mascota)

        return render(request, "AppLitobar/mascotas.html", {"mascotas": mascotas, "nombre_mascota": nombre_mascota})
    else:
        error_message = "No enviaste datos"
        return render(request, "AppLitobar/mascotas.html", {"error_message": error_message})
