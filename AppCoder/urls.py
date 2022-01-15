from django.urls import path
from AppCoder import views

urlpatterns = [

    # URLS PRINCIPALES

    path("", views.inicio, name='inicio'),
    path("cursos/", views.curso, name='curso'),
    path("profesores/", views.profesores, name='profesores'),
    path("estudiante/", views.estudiantes, name='estudiantes'),
    path("entregables/", views.entregables, name='entregables'),

    # URLS PARA CREACION

    path("CrearCurso/", views.crear_curso, name="CrearCurso"),
    path("CrearEstudiante/", views.crear_estudiante, name="CrearEstudiante"),
    path("CrarProfesor/", views.crear_profesor, name="CrearProfesor"),
    path("CrearEntregable/", views.crear_entregable, name="CrearEntregable"),

    # URLS PARA BUSQUEDA

    path("BuscarCamada/", views.buscar_camada, name="BuscarCamada"),
    path("Buscar/", views.buscar, name="Buscar"),


]
