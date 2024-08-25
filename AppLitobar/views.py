from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppLitobar.models import Cita, Mascota, Apoderado

# Create your views here.

def inicio(req):
    return render(req, "AppLitobar/daddy.html")

def cita(req):
    return render(req, "AppLitobar/cita.html")

def apoderado(req):
    return render(req, "AppLitobar/apoderados.html")

def mascotas(req):
    return render(req, "AppLitobar/mascotas.html")

def cita_formulario(req):
    if req.method == 'POST':
        # Crear un nuevo objeto Cita usando los datos del formulario
        cita = Cita(
            fecha=req.POST['cita'],
            motivo=req.POST['motivo'],
            veterinario=req.POST['veterinario']
        )
        cita.save()

        return redirect('inicio')

    return render(req, "AppLitobar/cita.html")

def mascotas_formulario(req):
    if req.method == 'POST':
        # Crear un nuevo objeto Cita usando los datos del formulario
        cita = Mascota(
            nombre_mascota=req.POST['nombre_mascota'],
            tipo=req.POST['tipo'],
            raza=req.POST['raza'],
            edad=req.POST['edad'],
        )
        cita.save()

        return redirect('inicio')

    return render(req, "AppLitobar/mascotas.html")


def apoderados_formulario(req):
    if req.method == 'POST':
        # Crear un nuevo objeto Cita usando los datos del formulario
        cita = Apoderado(
            nombre_apoderado=req.POST['nombre_apoderado'],
            apellido=req.POST['apellido'],
            email=req.POST['email'],
            telefono=req.POST['telefono'],
        )
        cita.save()

        return redirect('inicio')

    return render(req, "AppLitobar/apoderados.html")

def busqueda_mascota(request):
    return render(request, "AppLitobar/daddy.html")


def buscar(request):

    if request.GET["nombre_mascota"]:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        nombre_mascota = request.GET['nombre_mascota']

        mascotas = Mascota.objects.filter(nombre_mascota__icontains=nombre_mascota)

        return render(request, "AppLitobar/daddy.html", {"mascotas": mascotas, "nombre_mascota": nombre_mascota})
    else:
        error_message = "No enviaste datos"
        return render(request, "AppLitobar/daddy.html", {"error_message": error_message})
