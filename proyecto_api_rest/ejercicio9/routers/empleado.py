from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import authentication

router = APIRouter(prefix="/empleados", tags=["empleados"])

# entidad empleado
class Empleado(BaseModel):
    id: int
    nombre: str
    apellidos: str
    telefono: int
    correo: str
    num_cuenta: str
    id_tienda: int

# lista de empleados
empleados_list = [
    Empleado(id=1, nombre="Juan", apellidos="Perez", telefono=123456789, correo="juan.perez@example.com", num_cuenta="1234567890", id_tienda=1),
    Empleado(id=2, nombre="Maria", apellidos="Lopez", telefono=987654321, correo="maria.lopez@example.com", num_cuenta="0987654321", id_tienda=2),
    Empleado(id=3, nombre="Carlos", apellidos="Gomez", telefono=112233445, correo="carlos.gomez@example.com", num_cuenta="1122334455", id_tienda=3),
    Empleado(id=4, nombre="Ana", apellidos="Martinez", telefono=556677889, correo="ana.martinez@example.com", num_cuenta="5566778899", id_tienda=4),
    Empleado(id=5, nombre="Luis", apellidos="Rodriguez", telefono=667788990, correo="luis.rodriguez@example.com", num_cuenta="6677889900", id_tienda=5)
]

# obtener todos los empleados
@router.get("/")
def get_empleados():
    return empleados_list

# buscar por id
@router.get("/{id_empleado}")
def get_empleado_by_id(id_empleado: int):
    empleados = [e for e in empleados_list if e.id == id_empleado]
    if empleados:
        return empleados[0]
    else:
        raise HTTPException(status_code=404, detail="empleado not found")

# buscar por telefono
@router.get("/telefono/{telefono}")
def get_empleado_by_telefono(telefono: str):
    empleados = [e for e in empleados_list if e.telefono == telefono]
    if empleados:
        return empleados[0]
    else:
        return {"error": "empleado not found"}
    
# buscar por correo
@router.get("/correo/{correo}")
def get_empleado_by_correo(correo: str):
    empleados = [e for e in empleados_list if e.correo == correo]
    if empleados:
        return empleados[0]
    else:
        raise HTTPException(status_code=404, detail="empleado not found")
    
# buscar por num_cuenta
@router.get("/num_cuenta/{num_cuenta}")
def get_empleado_by_num_cuenta(num_cuenta: str):
    empleados = [e for e in empleados_list if e.num_cuenta == num_cuenta]
    if empleados:
        return empleados[0]
    else:
        return {"error": "empleado not found"}

# buscar por id_tienda
@router.get("/id_tienda/{id_tienda}")
def get_empleado_by_id_tienda(id_tienda: str):
    empleados = [e for e in empleados_list if e.id_tienda == id_tienda]
    if empleados:
        return empleados[0]
    else:
        return {"error": "empleado not found"}
    
# añadir un empleado
@router.post("/", status_code=201)
def add_empleado(empleado: Empleado, authorized = Depends(authentication)):
    empleado.id = next_id()
    empleados_list.append(empleado)
    return empleado

# modificar empleado
@router.put("/{id}", response_model=Empleado)
def modify_empleado(id: int, empleado: Empleado):
    for index, saved_empleado in enumerate(empleados_list):
        if saved_empleado.id == id:
            empleado.id = id
            empleados_list[index] = empleado
            return empleado
    raise HTTPException(status_code=404, detail="empleado not found")

# eliminar médico
@router.delete("/{id}")
def remove_empleado(id: int):
    for saved_empleado in empleados_list:
        if saved_empleado.id == id:
            empleados_list.remove(saved_empleado)
            return{}
    raise HTTPException(status_code=404, detail="empleado not found")

# obtiene el siguiente id
def next_id():
    # encuentra el id más grande en la lista y devuelve el siguiente valor
    return max([empleado.id for empleado in empleados_list], default=0) + 1
