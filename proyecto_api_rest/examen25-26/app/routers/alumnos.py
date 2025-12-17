from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from db.models.alumno import Alumno
from db.client import db_client
from db.schemas.alumno import alumno_schema, alumnos_schema

from bson import ObjectId

router = APIRouter(prefix="/alumnosdb", tags=["alumnosdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
alumnos_list = []

@router.get("/", response_model=list[Alumno])
async def alumnos():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return alumnos_schema(db_client.test.alumnos.find())

# Método get por id
@router.get("/{id}", response_model=Alumno)
async def alumno(id: str):
    return search_alumno_id(id)

@router.get("/colegios/{id_colegio}", response_model=Alumno)
async def alumno(id_colegio: str):
    return search_alumno_id_colegio(id_colegio)

@router.post("/", response_model=Alumno, status_code=201)
async def add_alumno(alumno: Alumno):
    #print("dentro de post")
    if type(search_alumno(alumno.nombre, alumno.apellidos)) == Alumno:
        raise HTTPException(status_code=409, detail="alumno already exists")
    
    alumno_dict = alumno.model_dump()
    del alumno_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.test.alumnos.insert_one(alumno_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    alumno_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo alumno a partir del diccionario alumno_dict
    return Alumno(**alumno_dict)
    
@router.put("/{id}", response_model=Alumno)
async def modify_alumno(id: str, new_alumno: Alumno):
    # Convertimos el usuario a un diccionario
    alumno_dict = new_alumno.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del alumno_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.test.alumnos.find_one_and_replace({"_id":ObjectId(id)}, alumno_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_alumno_id(id)    
    except:
        raise HTTPException(status_code=404, detail="alumno not found")
    

@router.delete("/{id}", response_model=Alumno)
async def delete_alumno(id:str):
    found = db_client.test.alumnos.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="alumno not found")
    return Alumno(**alumno_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_alumno_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        alumno = alumno_schema(db_client.test.alumnos.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto alumno. 
        return Alumno(**alumno)
    except:
        return {"error": "alumno not found"}

def search_alumno(nombre: str, apellidos: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto alumno. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        alumno = alumno_schema(db_client.test.alumnos.find_one({"nombre":nombre, "apellidos":apellidos}))
        return Alumno(**alumno)
    except:
        return {"error": "alumno not found"}

def search_alumno_id_colegio(id_colegio: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto alumno. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        alumno = alumno_schema(db_client.test.alumnos.find_one({"id_colegio":id_colegio}))
        return Alumno(**alumno)
    except:
        return {"error": "alumno not found"}

def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(alumno.id for alumno in alumnos_list))+1