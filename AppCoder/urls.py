from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio),
    path("cursos", views.curso),
    path("profesor", views.profesores),
    path("estudiante", views.estudiantes),

]