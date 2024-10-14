from typing import List
from datetime import datetime

from inventory.entities.entitiesInventory import Inventory


from inventory.interfaceAdapter.gateways.inventoryGateways import GatewaysInventory

class InventoryUseCase:
    def __init__(self, inventory_gateways = GatewaysInventory):
        self.inventory_gateways = inventory_gateways

    def get_inventory(self)-> Inventory:
        return self.inventory_gateways.get_inventorys()

    
    def create_inventory(self, producto:int, cantidad:int,bodega:str)->Inventory:
        return self.inventory_gateways.create_inventory(producto, cantidad, bodega)
    
    def get_byid_inventory(self,inventory_id:int)->Inventory:
        return self.inventory_gateways.get_byid_inventory(inventory_id)
