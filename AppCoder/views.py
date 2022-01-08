from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(self):

    curso = Curso(nombre="Desarrolo Web", camada="1998")
    curso.save()
    documentotxt= f"--->Curso: {curso.nombre} --->Camada: {curso.camada}"
    return HttpResponse(documentotxt)