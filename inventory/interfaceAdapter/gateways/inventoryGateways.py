from typing import List
from django.http import Http404
from inventory.entities.entitiesInventory import Inventory as EntitiesInventory
from products.repositorys.repositoryProducts import Productos
from datetime import datetime
from inventory.repositorys.repositoryInventory import Inventory



class GatewaysInventory:
    def __init__(self) ->None:
        self.inventory_repository =Inventory()
        self.products_repository =Productos()

    def get_inventorys(self)->List[EntitiesInventory]:
        orm_invetorys = self.inventory_repository.get_inventorys()
        inventorys = []

        for orm_inventory in orm_invetorys:
            inventorys.append(EntitiesInventory(producto=orm_inventory.producto, 
                            cantidad=orm_inventory.cantidad,
                            bodega=orm_inventory.bodega,
                            acutalizado_en=orm_inventory.actualizado_en))
        
        return inventorys

    
    def create_inventory(self, producto_id:int, cantidad:int, bodega:str)->EntitiesInventory:

        producto = self.products_repository.get_byid_product(producto_id)
        if producto:

            orm_inventory= self.inventory_repository.create_inventory(producto, cantidad, bodega)
            return EntitiesInventory(producto=orm_inventory.producto, 
                                    cantidad=orm_inventory.cantidad,
                                    bodega=orm_inventory.bodega,
                                    acutalizado_en=orm_inventory.actualizado_en)
        raise Http404
    

    def get_byid_inventory(self, inventory_id:int)->EntitiesInventory:
        orm_inventory = self.inventory_repository.get_byid_inventory(inventory_id)
        return EntitiesInventory(producto=orm_inventory.producto, 
                                    cantidad=orm_inventory.cantidad,
                                    bodega=orm_inventory.bodega,
                                    acutalizado_en=orm_inventory.actualizado_en)
        


