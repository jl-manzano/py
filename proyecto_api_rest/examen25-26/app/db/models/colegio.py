from typing import Optional
from pydantic import BaseModel

#Entidad Colegio
class Colegio(BaseModel):
    id: Optional[str]
    nombre: str
    distrito: str
    tipo: str
    direccion: str