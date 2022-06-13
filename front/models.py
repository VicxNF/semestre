from operator import mod
from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID de la categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name= 'Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='ID del producto')
    nombreProducto = models.CharField(max_length=60, verbose_name='Nombre del producto')
    imagen = models.CharField(max_length=100, verbose_name='Imagen del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombreProducto

# Create your models here.
class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    nombreFoto = models.CharField(max_length=100)
    nombreArchivo= models.CharField(max_length=256)
    descripcion=models.CharField(max_length=500)
    
    def __str__(self):
        return self.nombreFoto