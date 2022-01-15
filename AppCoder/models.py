from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre= models.CharField(max_length=12)
    camada= models.IntegerField()

    def __str__(self):

        return f"Curso: {self.nombre}"

class Estudiante(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):

        return f"Estudiante: {self.nombre} {self.apellido}"

class Profesor(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):

        return f"Profesor: {self.nombre} {self.apellido}"

class Entregable(models.Model):

    nombre= models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado= models.BooleanField()

    def __str__(self):

        return f"Entregable: {self.nombre}"