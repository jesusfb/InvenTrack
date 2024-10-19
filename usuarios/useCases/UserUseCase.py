from typing import List
from datetime import datetime

from usuarios.entities.entitiesUsuarios import Rol, DataUsuario,Users
from usuarios.interface_adapters.gateways.GatewaysUsers import GatewaysUsers

class UserUseCase:
    def __init__(self, usuarios_gateways = GatewaysUsers):
        self.usuarios_gateways = usuarios_gateways


    def get_rol(self)-> List[Rol]:
        return self.usuarios_gateways.get_roles()
    
    def get_byid_rol(self, rol_id)->Rol:
        return self.usuarios_gateways.get_rol_id(rol_id)

    

    def create_info_usuario(self, user_id:int, rol_id:int, direccion:str, ciudad:str,
                            pais:str, telefono:str) -> DataUsuario:
        return self.usuarios_gateways.create_info_usuario(user_id, rol_id, direccion, ciudad, pais, telefono)


    def get_user_byid(self, user_id:int)->Users:
        info_user = self.usuarios_gateways.get_user_byid(user_id)
        return info_user

    def get_users(self,)->List[Users]:
        return self.usuarios_gateways.get_users()
