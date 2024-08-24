# Generated by Django 5.1 on 2024-08-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apoderado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_apoderado", models.CharField(max_length=30)),
                ("apellido", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("telefono", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Cita",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("motivo", models.CharField(max_length=300)),
                ("veterinario", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Mascota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_mascota", models.CharField(max_length=40)),
                ("tipo", models.CharField(max_length=40)),
                ("raza", models.CharField(max_length=40)),
                ("edad", models.IntegerField()),
            ],
        ),
    ]
