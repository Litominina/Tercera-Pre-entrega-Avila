# Generated by Django 5.1 on 2024-09-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppLitobar", "0004_mascota_fecha_edit_mascota_fecha_new"),
    ]

    operations = [
        migrations.AddField(
            model_name="cita",
            name="imagen_mascota",
            field=models.ImageField(blank=True, null=True, upload_to="citas/"),
        ),
    ]
