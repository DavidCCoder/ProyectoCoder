from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from AppCoder.forms import CrearCurso

# Create your views here.

def inicio(request):
    
    return render(request, 'AppCoder/inicio.html')

def curso(request):
    
    return render(request, 'AppCoder/curso.html')

def padre(request):
    
    return render(request, 'AppCoder/padre.html')

def profesores(request):
    
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    
    return render(request, 'AppCoder/entregables.html')

def CrearCurso(request):

    if request.method == 'POST':

        Formulario = CrearCurso(request.POST)

        print(Formulario)

        if Formulario.is_valid:

            informacion = Formulario.clean_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "AppCoder/inicio.html")

    else:

        Formulario= CrearCurso()

    return render(request, "AppCoder/CrearCurso.html", {"Formulario":Formulario})


            