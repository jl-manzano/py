from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from db.models.empleado import Empleado
from db.client import db_client
from db.schemas.empleado import empleado_schema, empleados_schema

from bson import ObjectId

router = APIRouter(prefix="/empleadosdb", tags=["empleadosdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
empleados_list = []

@router.get("/", response_model=list[Empleado])
async def empleados():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return empleados_schema(db_client.otherdb.empleados.find())

# Método get por id
@router.get("/{id}", response_model=Empleado)
async def empleado(id: str):
    return search_empleado_id(id)


@router.post("/", response_model=Empleado, status_code=201)
async def add_empleado(empleado: Empleado):
    #print("dentro de post")
    if type(search_empleado(empleado.nombre, empleado.apellidos)) == Empleado:
        raise HTTPException(status_code=409, detail="empleado already exists")
    
    empleado_dict = empleado.model_dump()
    del empleado_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.otherdb.empleados.insert_one(empleado_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    empleado_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo empleado a partir del diccionario empleado_dict
    return Empleado(**empleado_dict)
    
@router.put("/{id}", response_model=Empleado)
async def modify_empleado(id: str, new_empleado: Empleado):
    # Convertimos el usuario a un diccionario
    empleado_dict = new_empleado.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del empleado_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.otherdb.empleados.find_one_and_replace({"_id":ObjectId(id)}, empleado_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_empleado_id(id)    
    except:
        raise HTTPException(status_code=404, detail="empleado not found")
    

@router.delete("/{id}", response_model=Empleado)
async def delete_empleado(id:str):
    found = db_client.otherdb.empleados.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="empleado not found")
    return Empleado(**empleado_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_empleado_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        empleado = empleado_schema(db_client.otherdb.empleados.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto empleado. 
        return Empleado(**empleado)
    except:
        return {"error": "empleado not found"}

def search_empleado(nombre: str, apellidos: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto empleado. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        empleado = empleado_schema(db_client.otherdb.empleados.find_one({"nombre":nombre, "apellidos":apellidos}))
        return Empleado(**empleado)
    except:
        return {"error": "empleado not found"}

def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(empleado.id for empleado in empleados_list))+1