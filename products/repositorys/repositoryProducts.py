from typing import List
from datetime import datetime
from inventory.models import Producto as ORMProducto
from django.utils.dateparse import parse_datetime  # Asegúrate de importar esta función si es la que usas
from django.db.models import Count
# from fixedVulnerability.models import FixedVulnerability as ORMFixed



class Productos:

    def __init__(self):
        pass

    def get_inventorys(self) ->List[ORMProducto]:
        return ORMProducto.objects.all()
    

    def get_byid_product(self, product_id:int)->ORMProducto:
        return ORMProducto.objects.get(id=product_id)
    
    # def create_inventory(self, producto, cantidad, bodega)->ORMInventario:
    #     return ORMInventario.objects.create(producto=producto, cantidad=cantidad,bodega=bodega)
