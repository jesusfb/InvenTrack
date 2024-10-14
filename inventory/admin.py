from django.contrib import admin

# Register your models here.
from .models import Inventario

@admin.register(Inventario)
class InventaryAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'bodega', 'actualizado_en')
    search_fields = ('producto', 'bodega',)
    list_filter= ('producto', 'bodega', 'actualizado_en')