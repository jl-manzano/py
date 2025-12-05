from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import authentication
from pymongo import MongoClient
from bson import ObjectId
from db.models.paciente import Patient
from db.client import db_client
from db.schemas.patient import patient_schema, patients_schema

from bson import ObjectId

router = APIRouter(prefix="/patientsdb", tags=["patientsdb"])

# Conexión a MongoDB
client = MongoClient()
db = client["healthcare"]
patients_collection = db["patients"]

# entidad paciente
class Patient(BaseModel):
    id: str
    dni: str
    apellidos: str
    nombre: str
    segsocial: str
    fnacimiento: str
    id_medico: str

# obtener todos los pacientes
@router.get("/")
async def get_patients():
    patients = list(patients_collection.find({}))
    for patient in patients:
        patient["id"] = str(patient["_id"])  # Convertir _id de MongoDB a string
        del patient["_id"]
    return patients

# buscar por id
@router.get("/{id_patient}")
async def get_patient_by_id(id_patient: str):
    patient = patients_collection.find_one({"_id": ObjectId(id_patient)})
    if patient:
        patient["id"] = str(patient["_id"])  # Convertir _id de MongoDB a string
        del patient["_id"]
        return patient
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# buscar por dni
@router.get("/dni/{dni_patient}")
async def get_patient_by_dni(dni_patient: str):
    patient = patients_collection.find_one({"dni": dni_patient})
    if patient:
        patient["id"] = str(patient["_id"])  # Convertir _id de MongoDB a string
        del patient["_id"]
        return patient
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# buscar por segsocial
@router.get("/segsocial/{segsocial_patient}")
async def get_patient_by_segsocial(segsocial_patient: str):
    patient = patients_collection.find_one({"segsocial": segsocial_patient})
    if patient:
        patient["id"] = str(patient["_id"])  # Convertir _id de MongoDB a string
        del patient["_id"]
        return patient
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# buscar por id_medico (para obtener los pacientes asignados a ese médico)
@router.get("/medico/{id_medico}")
async def get_patients_by_medico(id_medico: str):
    patients = list(patients_collection.find({"id_medico": id_medico}))
    if patients:
        for patient in patients:
            patient["id"] = str(patient["_id"])  # Convertir _id de MongoDB a string
            del patient["_id"]
        return patients
    else:
        raise HTTPException(status_code=404, detail="No patients found for this physician")

# añadir un paciente
@router.post("/", status_code=201)
async def add_patient(patient: Patient):
    patient_dict = patient.dict(exclude_unset=True)
    result = patients_collection.insert_one(patient_dict)
    patient.id = str(result.inserted_id)
    return patient

# modificar paciente
@router.put("/{id}", response_model=Patient)
async def modify_patient(id: str, patient: Patient):
    patient_dict = patient.dict(exclude_unset=True)
    result = patients_collection.update_one({"_id": ObjectId(id)}, {"$set": patient_dict})
    if result.modified_count > 0:
        updated_patient = patients_collection.find_one({"_id": ObjectId(id)})
        updated_patient["id"] = str(updated_patient["_id"])
        del updated_patient["_id"]
        return updated_patient
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# eliminar paciente
@router.delete("/{id}")
async def remove_patient(id: str):
    result = patients_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return {}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
