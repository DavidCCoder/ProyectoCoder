from django import forms

class form_curso(forms.Form):

    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class form_estudiante(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class form_profesor(forms.Form):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class form_entregable(forms.Form):

    nombre= forms.CharField(max_length=30)
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()

