from typing import List
from datetime import datetime
from inventory.models import Inventario as ORMInventario
from django.utils.dateparse import parse_datetime  # Asegúrate de importar esta función si es la que usas
from django.db.models import Count
# from fixedVulnerability.models import FixedVulnerability as ORMFixed



class Inventory:

    def __init__(self):
        pass

    def get_inventorys(self) ->List[ORMInventario]:
        return ORMInventario.objects.all()
    
    def create_inventory(self, producto, cantidad, bodega)->ORMInventario:
        return ORMInventario.objects.create(producto=producto, cantidad=cantidad,bodega=bodega)
    
    def get_byid_inventory(self, inventory_id:int)->ORMInventario:
        return ORMInventario.objects.filter(id=inventory_id).get()
