from django.db import models

# Create your models here.

class Peliculas(models.Model):

    titulo=models.TextField(max_length=50)
    genero=models.TextField(max_length=20)
    year=models.IntegerField()
    cant_copias=models.IntegerField()

class Clientes(models.Model):
    
    nombre=models.TextField(max_length=30)
    apellidos=models.TextField(max_length=30)
    rut=models.TextField(max_length=12)
    telefono=models.TextField(max_length=15)
    email=models.EmailField()

class Usuarios(models.Model):
    nombre=models.TextField(max_length=20)
    apellidos=models.TextField(max_length=30)
    telefono=models.TextField(max_length=15)
    cargo=models.TextField(max_length=20)

class Arriendos(models.Model):
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    idPelicula=models.IntegerField(null=True)
    idCliente=models.IntegerField(null=True)




