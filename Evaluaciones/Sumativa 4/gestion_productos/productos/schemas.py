from pydantic import BaseModel
from typing import List

class ProductoSchema(BaseModel):
    codigo: str
    nombre: str
    precio: float
    marca_id: int
    categoria_id: int
    caracteristicas_ids: List[int]
