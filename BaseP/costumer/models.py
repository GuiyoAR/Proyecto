from tabnanny import verbose
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pasaporte = models.IntegerField()
    vencimiento = models.DateField()
    dni = models.IntegerField(unique=True)
    domicilio = models.CharField(max_length=40)
    telefono = models.IntegerField()
    activo = models.BooleanField(default=True)

class Meta:
    verbose_name = 'cliente'
    verbose_name_plural = 'clientes'

def __str__(self):
    return self.nombre + self.apellido 