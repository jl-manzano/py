from typing import Optional
from pydantic import BaseModel

# Entidad user
class User(BaseModel):
    username: Optional[str] = None
    fullname:str
    email:str
    disabled: bool
    password: str