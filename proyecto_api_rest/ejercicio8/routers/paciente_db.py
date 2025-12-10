from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from db.models.paciente import Patient
from db.client import db_client
from db.schemas.patient import patient_schema, patients_schema

from bson import ObjectId

router = APIRouter(prefix="/patientsdb", tags=["patientsdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
patients_list = []

@router.get("/", response_model=list[Patient])
async def patients():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return patients_schema(db_client.test.patients.find())

# Método get por id
@router.get("/{id}", response_model=Patient)
async def patient(id: str):
    return search_patient_id(id)


@router.post("/", response_model=Patient, status_code=201)
async def add_patient(patient: Patient):
    #print("dentro de post")
    if type(search_patient(patient.dni)) == Patient:
        raise HTTPException(status_code=409, detail="Patient already exists")
    
    patient_dict = patient.model_dump()
    del patient_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.test.patients.insert_one(patient_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    patient_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo patient a partir del diccionario patient_dict
    return Patient(**patient_dict)
    
@router.put("/{id}", response_model=Patient)
async def modify_patient(id: str, new_patient: Patient):
    # Convertimos el usuario a un diccionario
    patient_dict = new_patient.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del patient_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.test.patients.find_one_and_replace({"_id":ObjectId(id)}, patient_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_patient_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Patient not found")
    

@router.delete("/{id}", response_model=Patient)
async def delete_patient(id:str):
    found = db_client.test.patients.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Patient not found")
    return Patient(**patient_schema(found))
   
# El id de la base de datos es un string, ya no es un entero
def search_patient_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        patient = patient_schema(db_client.test.patients.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto patient. 
        return Patient(**patient)
    except:
        return {"error": "Patient not found"}

def search_patient(dni: str):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto patient. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        patient = patient_schema(db_client.test.patients.find_one({"dni":dni}))
        return Patient(**patient)
    except:
        return {"error": "Patient not found"}

def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(patient.id for patient in patients_list))+1