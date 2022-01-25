from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from AppCoder.forms import FormCurso, FormEstudiante, FormProfesor, FormEntregable

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

        Formulario = FormCurso(request.POST)

        if Formulario.is_valid():

            informacion = Formulario.cleaned_data

            curso = Curso(
                nombre=informacion['curso'], camada=informacion['camada'])

            curso.save()

            return render(request, "AppCoder/inicio.html")

    else:

        Formulario = FormCurso()

    return render(request, "AppCoder/crear_curso.html", {"Formulario": Formulario})


def crear_estudiante(request):

    if request.method == 'POST':

        FormularioEstudiantes = FormEstudiante(request.POST)

        if FormularioEstudiantes.is_valid():

            info = FormularioEstudiantes.cleaned_data

            estudiante = Estudiante(
                nombre=info['nombre'], apellido=info['apellido'], email=info['email'])

            estudiante.save()

            return render(request, "AppCoder/inicio.html")

    else:

        FormularioEstudiantes = FormEstudiante()

    return render(request, "AppCoder/crear_estudiante.html", {"FormularioEstudiantes": FormularioEstudiantes})


def crear_profesor(request):

    if request.method == 'POST':

        FormularioProfesor = FormProfesor(request.POST)

        if FormularioProfesor.is_valid():

            info = FormularioProfesor.cleaned_data

            profesor = Profesor(nombre=info['nombre'], apellido=info['apellido'],
                                email=info['email'], profesion=info['profesion'])

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:

        FormularioProfesor = FormProfesor()

    return render(request, "AppCoder/crear_profesor.html", {"FormularioProfesor": FormularioProfesor})


def crear_entregable(request):

    if request.method == 'POST':

        FormularioEntregable = FormEntregable(request.POST)

        if FormularioEntregable.is_valid():

            info = FormularioEntregable.cleaned_data

            entregable = Entregable(
                nombre=info['nombre'], fechaDeEntrega=info['fecha_entrega'], entregado=info['entregado'])

            entregable.save()

            return render(request, "AppCoder/inicio.html")

    else:

        FormularioEntregable = FormEntregable()

    return render(request, "AppCoder/crear_entregable.html", {"FormularioEntregable": FormularioEntregable})


# VIEWS PARA BUSQUEDA


def buscar_camada(request):

    return render(request, "AppCoder/buscar_camada.html")


def buscar(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada)

        return render(request, "AppCoder/RTbuscar_camada.html", {"cursos": cursos, "camada": camada})

    else:

        respuesta = "No enviaste los datos correctos"

    return render(request, "AppCoder/inicio.html", {"respuesta": respuesta})
