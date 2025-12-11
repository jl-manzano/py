from typing import Optional
from pydantic import BaseModel

#Entidad empleado
class Empleado(BaseModel):
    id: Optional[str]
    nombre: str
    apellidos: str
    telefono: int
    correo: str
    num_cuenta: str
    id_tienda: str
