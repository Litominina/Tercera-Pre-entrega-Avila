from django.db import models
from django.utils import timezone

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    veterinario = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se guarda solo al crear
    fecha_modificacion = models.DateTimeField(auto_now=True)  # Se actualiza cada vez que se edita
    imagen_mascota = models.ImageField(upload_to='citas/', blank=True, null=True)


    def __str__(self):
        return f"Cita de {self.veterinario} para {self.motivo} con {self.veterinario}"

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    fecha_new = models.DateTimeField(auto_now_add=True)  # Se guarda solo al crear
    fecha_edit = models.DateTimeField(auto_now=True)  # Se actualiza cada vez que se edita

    def __str__(self):
        return f"Nombre mascota: {self.nombre_mascota} - Tipo animal: {self.tipo} - Raza: {self.raza} - Edad: {self.edad}"
    

class Apoderado(models.Model):
    nombre_apoderado = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre_apoderado} - Apellido: {self.apellido} - Email: {self.email} - Teléfono: {self.telefono}"