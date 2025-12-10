from typing import Optional
from pydantic import BaseModel

#Entidad physician
class Patient(BaseModel):
    id: Optional[str]
    dni: str
    apellidos: str
    nombre: str
    segsocial: str
    fnacimiento: str
    id_medico: Optional[str]
