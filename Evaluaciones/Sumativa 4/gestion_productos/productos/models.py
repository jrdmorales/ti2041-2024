from django.db import models

class Marca(models.Model):
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=100)

class Categoria(models.Model):
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=100)

class Caracteristica(models.Model):
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    def __str__(self):
        return self.nombre
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    caracteristicas = models.ManyToManyField(Caracteristica)
