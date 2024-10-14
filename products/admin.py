from django.contrib import admin

# Register your models here.
from .models import Producto


@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display =('nombre','descripcion', 'precio', 'creado_en')
    search_fields = ('nombre',)
    list_filter = ('nombre', 'creado_en')
