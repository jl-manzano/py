from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import authentication

router = APIRouter(prefix="/tiendas", tags=["tiendas"])

# entidad tienda
class Tienda(BaseModel):
    id: int
    domicilio: str
    telefono: int
    precio_alquiler: float

# lista de tiendas
tiendas_list = [
    Tienda(id=1, domicilio="Calle Falsa 123, Ciudad A", telefono=555123456, precio_alquiler=1500.50),
    Tienda(id=2, domicilio="Avenida Siempre Viva 456, Ciudad B", telefono=555987654, precio_alquiler=2000.00),
    Tienda(id=3, domicilio="Boulevard Central 789, Ciudad C", telefono=555456789, precio_alquiler=1200.75),
    Tienda(id=4, domicilio="Calle Mayor 101, Ciudad D", telefono=555321987, precio_alquiler=1800.25),
    Tienda(id=5, domicilio="Plaza de la Libertad 202, Ciudad E", telefono=555654321, precio_alquiler=2200.40)
]
# obtener todas las tiendas
@router.get("/")
def get_tiendas():
    return tiendas_list

# buscar por id
@router.get("/{id_tienda}")
def get_tienda_by_id(id_tienda: int):
    tiendas = [t for t in tiendas_list if t.id == id_tienda]
    if tiendas:
        return tiendas[0]
    else:
        raise HTTPException(status_code=404, detail="tienda not found")
    
# añadir una tienda
@router.post("/", status_code=201)
def add_tienda(tienda: Tienda, authorized = Depends(authentication)):
    tienda.id = next_id()
    tiendas_list.append(tienda)
    return tienda

# modificar tienda
@router.put("/{id}", response_model=Tienda)
def modify_tienda(id: int, tienda: Tienda):
    for index, saved_tienda in enumerate(tiendas_list):
        if saved_tienda.id == id:
            tienda.id = id
            tiendas_list[index] = tienda
            return tienda
    raise HTTPException(status_code=404, detail="tienda not found")

# eliminar médico
@router.delete("/{id}")
def remove_tienda(id: int):
    for saved_tienda in tiendas_list:
        if saved_tienda.id == id:
            tiendas_list.remove(saved_tienda)
            return{}
    raise HTTPException(status_code=404, detail="tienda not found")

# obtiene el siguiente id
def next_id():
    # encuentra el id más grande en la lista y devuelve el siguiente valor
    return max([tienda.id for tienda in tiendas_list], default=0) + 1
