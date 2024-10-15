from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='informacion_usuario')
    rol = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}, {self.pais}"

