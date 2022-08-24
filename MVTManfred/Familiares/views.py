from datetime import datetime

from django.shortcuts import render

from Familiares.models import Familiares

def familiares(request):

    fecharegistro = datetime.now()

    familiar1 = Familiares(nombre="Lorena", apellidos="Peñuela Gonzalez", telefono="3114572365", fecha_registro=fecharegistro)
    familiar1.save()

    familiar2 = Familiares(nombre="Anderson", apellidos="Romero Rico", telefono="3005487455", fecha_registro=fecharegistro)
    familiar2.save()

    familiar3 = Familiares(nombre="Luciana", apellidos="Romero Peñuela", telefono="3155689415", fecha_registro=fecharegistro)
    familiar3.save()

    contexto = {
            "familiar1": familiar1,
            "familiar2": familiar2,
            "familiar3": familiar3
          }

    return render(request, 'familiares.html', contexto)

