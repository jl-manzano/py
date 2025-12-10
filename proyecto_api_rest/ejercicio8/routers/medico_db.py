from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from db.models.medico import Physician
from db.client import db_client
from db.schemas.medico import physician_schema, physicians_schema

from bson import ObjectId

router = APIRouter(prefix="/physiciansdb", tags=["physiciansdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
physicians_list = []

@router.get("/", response_model=list[Physician])
async def physicians():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return physicians_schema(db_client.test.physicians.find())

# Método get por id
@router.get("/{id}", response_model=Physician)
async def physician(id: str):
    return search_physician_id(id)


@router.post("/", response_model=Physician, status_code=201)
async def add_physician(physician: Physician):
    #print("dentro de post")
    if type(search_physician(physician.name, physician.surname)) == Physician:
        raise HTTPException(status_code=409, detail="Physician already exists")
    
    physician_dict = physician.model_dump()
    del physician_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.test.physicians.insert_one(physician_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    physician_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo physician a partir del diccionario physician_dict
    return Physician(**physician_dict)
    
@router.put("/{id}", response_model=Physician)
async def modify_physician(id: str, new_physician: Physician):
    # Convertimos el usuario a un diccionario
    physician_dict = new_physician.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del physician_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.test.physicians.find_one_and_replace({"_id":ObjectId(id)}, physician_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_physician_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Physician not found")
    

@router.delete("/{id}", response_model=Physician)
async def delete_physician(id:str):
    found = db_client.test.physicians.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Physician not found")
    return Physician(**physician_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_physician_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        physician = physician_schema(db_client.test.physicians.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto physician. 
        return Physician(**physician)
    except:
        return {"error": "Physician not found"}

def search_physician(name: str, surname: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto physician. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        physician = physician_schema(db_client.test.physicians.find_one({"name":name, "surname":surname}))
        return Physician(**physician)
    except:
        return {"error": "Physician not found"}

def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(physician.id for physician in physicians_list))+1