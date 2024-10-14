from django.db import models
from products.models import Producto
# Create your models here.
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    bodega = models.CharField(max_length=255)
    actualizado_en = models.DateTimeField(auto_now=True)