from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from db.models.tienda import Tienda
from db.client import db_client
from db.schemas.tienda import tienda_schema, tiendas_schema

from bson import ObjectId

router = APIRouter(prefix="/tiendasdb", tags=["tiendasdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
tiendas_list = []

@router.get("/", response_model=list[Tienda])
async def tiendas():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return tiendas_schema(db_client.otherdb.tiendas.find())

# Método get por id
@router.get("/{id}", response_model=Tienda)
async def tiendas(id: str):
    return search_tienda_id(id)


@router.post("/", response_model=Tienda, status_code=201)
async def add_tiendas(tiendas: Tienda):
    #print("dentro de post")
    if type(search_tienda(tiendas.id)) == Tienda:
        raise HTTPException(status_code=409, detail="tiendas already exists")
    
    tiendas_dict = tiendas.model_dump()
    del tiendas_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.otherdb.tiendas.insert_one(tiendas_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    tiendas_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo tiendas a partir del diccionario tiendas_dict
    return Tienda(**tiendas_dict)
    
@router.put("/{id}", response_model=Tienda)
async def modify_tiendas(id: str, new_tiendas: Tienda):
    # Convertimos el usuario a un diccionario
    tiendas_dict = new_tiendas.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del tiendas_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.otherdb.tiendas.find_one_and_replace({"_id":ObjectId(id)}, tiendas_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_tienda_id(id)    
    except:
        raise HTTPException(status_code=404, detail="tiendas not found")
    
@router.delete("/{id}", response_model=Tienda)
async def delete_tienda(id:str):
    found = db_client.otherdb.tiendas.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="tienda not found")
    return Tienda(**tienda_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_tienda_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        tienda = tienda_schema(db_client.otherdb.tiendas.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto tienda. 
        return Tienda(**tienda)
    except:
        return {"error": "tienda not found"}

def search_tienda(id: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto tienda. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        tienda = tienda_schema(db_client.otherdb.tiendas.find_one({"id":id}))
        return Tienda(**tienda)
    except:
        return {"error": "tienda not found"}

def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(tiendas.id for tiendas in tiendas_list))+1