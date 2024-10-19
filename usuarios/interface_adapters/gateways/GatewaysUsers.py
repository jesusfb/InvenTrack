from typing import List

from django.contrib.auth.middleware import get_user
from django.http import Http404
from datetime import datetime
from usuarios.entities.entitiesUsuarios import Rol, DataUsuario, Users
from usuarios.repositories.usuarioRepository import Roles, Direcciones
from django.contrib.auth.models import User, AbstractUser

class GatewaysUsers:
    def __init__(self):
        self.roles_repository = Roles()
        self.direcciones_repository = Direcciones()

    def get_roles(self)->List[Rol]:
        orm_roles = self.roles_repository.get_rol()

        roles= []

        for orm_rol in orm_roles:
            roles.append(Rol(nombre= orm_rol.nombre))
        
        return roles

    def get_rol_id(self,rol_id:int)->Rol:
        orm_rol = self.roles_repository.get_rol_byid(rol_id)

        return Rol(nombre=orm_rol.nombre)
    

    def get_user(self, user_id:int):
        return User.objects.get(id=user_id)

    def create_info_usuario(self, user_id:int, rol_id:int, direccion:str, ciudad:str,
                            pais:str, telefono:str)->DataUsuario:
        rol = self.roles_repository.get_rol_byid(rol_id)
        user = self.get_user(user_id)
        if rol and user:
            orm_datausuario = self.direcciones_repository.create_direcciones(user, rol, direccion, ciudad,pais,telefono)
            return DataUsuario(user_id= orm_datausuario.usuario, rol= orm_datausuario.rol,
                               direccion=orm_datausuario.direccion, ciudad=orm_datausuario.ciudad,
                               pais=orm_datausuario.pais, telefono=orm_datausuario.telefono)


    def get_user_byid(self, id:int)-> Users:

        try:
            usuario = User.objects.get(id = id)

            if usuario:
                info_usuario = self.direcciones_repository.get_direcciones_by_user(usuario.id).first()
                return Users ( users_id= usuario.id,
                    first_name= usuario.first_name,
                    last_name= usuario.last_name,
                    email= usuario.email,
                   cellphone=info_usuario.telefono if info_usuario else None,
                   country=info_usuario.ciudad if info_usuario else None,
                   direction=info_usuario.direccion if info_usuario else None
                )
        except User.DoesNotExist:
            raise Http404("User not found")

    def get_users(self)->List[Users]:
        try:
            usuarios = User.objects.all()
            list_users=[]
            if usuarios:
                for usuario in usuarios:
                    direcciones= self.direcciones_repository.get_direcciones_by_user(usuario.id).first()
                    print(direcciones)
                    list_users.append(Users(users_id= usuario.id,
                           first_name=usuario.first_name,
                           last_name=usuario.last_name,
                           email=usuario.email,
                           cellphone=direcciones.telefono if direcciones else None,
                           country= direcciones.ciudad if direcciones else None,
                           direction=direcciones.direccion if direcciones else None
                   ))
                return list_users
        except User.DoesNotExist:
            raise Http404("users not fount")