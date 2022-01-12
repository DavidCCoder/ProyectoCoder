from django import forms

class CrearCurso(forms.Form):

    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()
