from django.db import models

# Create your models here.
class Cita(models.Model):
    fecha = models.DateField()
    motivo = models.CharField(max_length=300)
    veterinario = models.CharField(max_length=40)

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()

class Apoderado(models.Model):
    nombre_apoderado = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()