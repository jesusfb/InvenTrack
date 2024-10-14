from dataclasses import dataclass
from typing import List
from datetime import datetime



@dataclass
class Inventory:
    producto:str
    cantidad:str
    bodega:str
    acutalizado_en:datetime
    