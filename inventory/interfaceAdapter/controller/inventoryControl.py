from django.http import Http404
from inventory.interfaceAdapter.gateways.inventoryGateways import GatewaysInventory
from inventory.usesCases.inventoryUseCase import InventoryUseCase
class ControlIventory():
    notfount = "No hay hay registros de inventario"
    def __init__(self):
        self.notfount = ControlIventory.notfount
        self.inventory_gateway= GatewaysInventory()
        self.inventory_usecase = InventoryUseCase(self.inventory_gateway)

    
    def get_all_inventory(self,):
        response = self.inventory_usecase.get_inventory()
        if response:
            return response
        
        raise Http404(self.notfount)

    
    def create_register_inventory(self, producto, cantidad, bodega):
        response = self.inventory_usecase.create_inventory(producto, cantidad, bodega)

        return response

    def get_byid_inventory(self, inventory_id:int):
        response  = self.inventory_usecase.get_byid_inventory(inventory_id)
        try:
            # Asegúrate de que `Inventario.objects.get` lanza un DoesNotExist si no lo encuentra
            return response
        except response:
            raise Http404("Inventario no encontrado")
    
   
