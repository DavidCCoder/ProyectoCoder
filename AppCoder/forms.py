from django import forms
from datetime import datetime


class FormCurso(forms.Form):

    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()


class FormEstudiante(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class FormProfesor(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class FormEntregable(forms.Form):

    nombre = forms.CharField(max_length=30)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField(required=False)
