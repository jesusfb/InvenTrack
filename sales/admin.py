from django.contrib import admin

# Register your models here.
from sales.models import Venta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto','cantidad', 'precio_total', 'fecha_venta')
    search_fields  = ('producto',)
    list_filter = ("fecha_venta",)