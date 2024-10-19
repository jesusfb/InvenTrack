from usuarios.interface_adapters.gateways.GatewaysUsers import GatewaysUsers
from usuarios.useCases.UserUseCase import UserUseCase
class ControlUsers:
    def __init__(self):
        self.user_gateway = GatewaysUsers()
        self.user_usecase = UserUseCase(self.user_gateway)


    def create_register_user(self, rol_id:str, direccion:str, ciudad:str, pais:str, telefono:str, user_id:int):
        return self.user_usecase.create_info_usuario( user_id, rol_id, direccion, ciudad, pais, telefono)
    

    def get_roles(self):
        return self.user_usecase.get_rol()
    


    def get_user_byid(self, user_id:int):

        return self.user_usecase.get_user_byid(user_id)

    def get_users(self, ):

        return self.user_usecase.get_users()