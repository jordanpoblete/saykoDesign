
from django.db import models

# Create your models here.


#Modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la Categoría")

    def __str__(self):
        return self.nombreCategoria

#Modelo para peticiones
class Peticion(models.Model):
    idPeticion= models.IntegerField(primary_key=True, verbose_name='Id de Peticion')
    correo= models.CharField(max_length=60,  verbose_name="correo")
    descripcion= models.CharField(max_length=600,  verbose_name="descripcion")
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.correo

#Modelo para ilustraciones 

class IlustracionIlu(models.Model):
    idIlustracion= models.IntegerField(primary_key=True, verbose_name='Id de Ilustracion')
    nombre= models.CharField(max_length=100,  verbose_name="nombre")
    descripcionIlu= models.CharField(max_length=600,  verbose_name="descripcion")
    fecha= models.DateField(verbose_name="fecha")
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to = "core", default="core/no-hay-imagen.jpg", verbose_name="imagen")

    def __str__(self):
        return self.nombre