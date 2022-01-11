from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("cursos", views.curso, name='curso'),
    path("profesores", views.profesores, name='profesores'),
    path("estudiante", views.estudiantes, name='estudiantes'),
    path("entregables", views.entregables, name='entregables'),

]