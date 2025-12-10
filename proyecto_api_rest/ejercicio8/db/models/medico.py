from typing import Optional
from pydantic import BaseModel

#Entidad physician
class Physician(BaseModel):
    id: Optional[str]
    name: str
    surname: str
    ncolegiado: str
    speciality: str
