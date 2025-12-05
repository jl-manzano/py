from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import authentication
from pymongo import MongoClient
from bson import ObjectId
from db.models.medico import Physician
from db.client import db_client
from db.schemas.medico import physician_schema, physicians_schema

from bson import ObjectId

router = APIRouter(prefix="/physiciansdb", tags=["physiciansdb"])

# Conexión a MongoDB
client = MongoClient()
db = client["healthcare"]
physicians_collection = db["physicians"]

# entidad médico
class Physician(BaseModel):
    id: str
    name: str
    surname: str
    ncolegiado: str
    speciality: str

# obtener todos los médicos
@router.get("/")
async def get_physicians():
    physicians = list(physicians_collection.find({}))
    for physician in physicians:
        physician["id"] = str(physician["_id"])  # Convertir _id de MongoDB a string
        del physician["_id"]
    return physicians

# buscar por id
@router.get("/{id_physician}")
async def get_physician_by_id(id_physician: str):
    physician = physicians_collection.find_one({"_id": ObjectId(id_physician)})
    if physician:
        physician["id"] = str(physician["_id"])  # Convertir _id de MongoDB a string
        del physician["_id"]
        return physician
    else:
        raise HTTPException(status_code=404, detail="Physician not found")

# buscar por ncolegiado
@router.get("/ncolegiado/{ncolegiado_physician}")
async def get_physician_by_ncolegiado(ncolegiado_physician: str):
    physician = physicians_collection.find_one({"ncolegiado": ncolegiado_physician})
    if physician:
        physician["id"] = str(physician["_id"])  # Convertir _id de MongoDB a string
        del physician["_id"]
        return physician
    else:
        raise HTTPException(status_code=404, detail="Physician not found")

# añadir un médico
@router.post("/", status_code=201)
async def add_physician(physician: Physician):
    physician_dict = physician.dict(exclude_unset=True)
    result = physicians_collection.insert_one(physician_dict)
    physician.id = str(result.inserted_id)
    return physician

# modificar médico
@router.put("/{id}", response_model=Physician)
async def modify_physician(id: str, physician: Physician):
    physician_dict = physician.dict(exclude_unset=True)
    result = physicians_collection.update_one({"_id": ObjectId(id)}, {"$set": physician_dict})
    if result.modified_count > 0:
        updated_physician = physicians_collection.find_one({"_id": ObjectId(id)})
        updated_physician["id"] = str(updated_physician["_id"])
        del updated_physician["_id"]
        return updated_physician
    else:
        raise HTTPException(status_code=404, detail="Physician not found")

# eliminar médico
@router.delete("/{id}")
async def remove_physician(id: str):
    result = physicians_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return {}
    else:
        raise HTTPException(status_code=404, detail="Physician not found")
