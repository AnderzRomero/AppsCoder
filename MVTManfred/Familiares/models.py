from django.db import models

class Familiares(models.Model):

    nombre=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=60)
    telefono=models.IntegerField()
    fecha_registro=models.DateField()
