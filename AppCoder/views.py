from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def curso(request):
    
    return render(request, 'AppCoder/curso.html')

def padre(request):
    
    return render(request, 'AppCoder/padre.html')

def profesores(request):
    
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    
    return render('AppCoder/estuadiantes.html')

def entregables(request):
    
    return render('AppCoder/entregables.html')