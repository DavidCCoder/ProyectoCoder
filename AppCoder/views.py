from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from AppCoder.forms import form_curso, form_estudiante, form_profesor, form_entregable

# VIEWS POR DEFECTO

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

# VIEWS PARA BOTONES Y CREACION

def crear_curso(request):

    if request.method == 'POST':

        Formulario = form_curso(request.POST)

        print(Formulario)

        if Formulario.is_valid:

            informacion = Formulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "AppCoder/inicio.html")

    else:

        Formulario= form_curso()

    return render(request, "AppCoder/CrearCurso.html", {"Formulario":Formulario})



def crear_estudiante(request):

    if request.method == 'POST':

        FormularioEstudiantes = form_estudiante(request.POST)

        print(FormularioEstudiantes)

        if FormularioEstudiantes.is_valid:

            info = FormularioEstudiantes.cleaned_data

            estudiante = Estudiante(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])

            estudiante.save()

            return render(request, "AppCoder/inicio.html")

    else:

        FormularioEstudiantes= form_estudiante()

    return render(request, "AppCoder/CrearEstudiante.html", {"FormularioEstudiantes":FormularioEstudiantes})



def crear_profesor(request):

    if request.method == 'POST':

        FormularioProfesor = form_profesor(request.POST)

        print(FormularioProfesor)

        if FormularioProfesor.is_valid:

            info = FormularioProfesor.cleaned_data

            profesor = Profesor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], profesion=info['profesion'])

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:

        FormularioProfesor= form_profesor()

    return render(request, "AppCoder/CrearProfesor.html", {"FormularioProfesor":FormularioProfesor})



def crear_entregable(request):

    if request.method == 'POST':

        FormularioEntregable = form_entregable(request.POST)

        print(FormularioEntregable)

        if FormularioEntregable.is_valid:

            info = FormularioEntregable.cleaned_data

            entregable = Entregable(nombre=info['nombre'], fechaDeEntrega=info['fecha_entrega'], entregado=info['entregado'])

            entregable.save()

            return render(request, "AppCoder/inicio.html")

    else:

        FormularioEntregable= form_entregable()

    return render(request, "AppCoder/CrearEntregable.html", {"FormularioEntregable":FormularioEntregable})


# VIEWS PARA BUSQUEDA


def buscar_camada(request):

    return render(request, "AppCoder/BuscarCamada.html")

def buscar(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada)

        return render(request, "AppCoder/RTBuscarCamada.html", {"cursos":cursos, "camada":camada})

    else:

        respuesta = "No enviaste los datos correctos"

    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})


            