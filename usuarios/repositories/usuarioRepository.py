from typing import List
from datetime import datetime
from django.utils.dateparse import parse_datetime  # Asegúrate de importar esta función si es la que usas
from django.db.models import Count
from usuarios.models import Rol as ORMRol, Direccion as ORMDireccion
from django.contrib.auth.models import User

class Roles:
    def __init__(self):
        pass

    def get_rol(self)->List[ORMRol]:
        return ORMRol.objects.all()
   
    def get_rol_byid(self, rol_id:int)->ORMRol:
        return ORMRol.objects.filter(id = int)
    
    def create_rol(self, nombre:str)->ORMRol:
        return ORMRol.objects.create(nombre = nombre)
    


class Direcciones:
    def __init__(self):
        pass

    def get_direcciones(self)->List[ORMDireccion]:
        return ORMDireccion.objects.all()
   
    def get_direcciones_by_user(self, user_id)->ORMDireccion:
        return ORMDireccion.objects.filter(usuario = user_id)
    
    def create_direcciones(self, user, rol, direccion, ciudad,pais,telefon)->ORMDireccion:
        return ORMDireccion.objects.create(usuario= user, rol=rol , direccion =direccion , ciudad = ciudad, pais= pais, telefono=telefon )
    
    
    
