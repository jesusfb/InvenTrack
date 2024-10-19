from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Rol:
    nombre:str


@dataclass
class DataUsuario:
    user_id:int
    rol:str
    direccion:str
    ciudad:str
    pais:str
    telefono:str
    #usuario:str


@dataclass
class Users:
    users_id:int
    first_name:str
    last_name:str
    email:str
    cellphone:str
    direction:str
    country:str
