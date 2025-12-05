from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import authentication

router = APIRouter(prefix="/physicians", tags=["physicians"])

# entidad médico
class Physician(BaseModel):
    id: int
    name: str
    surname: str
    ncolegiado: str
    speciality: str

# lista de médicos
physicians_list = [
    Physician(id=1, name="Natan", surname="de Souza", ncolegiado="M-12345", speciality="Cardiología"),
    Physician(id=2, name="Antony", surname="dos Santos", ncolegiado="M-23456", speciality="Neurología"),
    Physician(id=3, name="Pablo", surname="Fornals", ncolegiado="M-34567", speciality="Pediatría"),
    Physician(id=4, name="Francisco Román", surname="Alarcón Suárez", ncolegiado="M-45678", speciality="Oncología")
]

# obtener todos los médicos
@router.get("/")
def get_medicos():
    return physicians_list

# buscar por id
@router.get("/{id_physician}")
def get_physician_by_id(id_physician: int):
    physicians = [p for p in physicians_list if p.id == id_physician]
    if physicians:
        return physicians[0]
    else:
        raise HTTPException(status_code=404, detail="Physician not found")


# buscar por ncolegiado
@router.get("/ncolegiado/{ncolegiado_physician}")
def get_physician_by_ncolegiado(ncolegiado_physician: str):
    physicians = [p for p in physicians_list if p.ncolegiado == ncolegiado_physician]
    if physicians:
        return physicians[0]
    else:
        return {"error": "Physician not found"}
    
# buscar por especialidad
@router.get("/speciality/{speciality_physician}")
def get_physician_by_speciality(speciality_physician: str):
    physicians = [p for p in physicians_list if p.speciality == speciality_physician]
    if physicians:
        return physicians[0]
    else:
        raise HTTPException(status_code=404, detail="Physician not found")
    
# añadir un médico
@router.post("/", status_code=201)
def add_physician(physician: Physician, authorized = Depends(authentication)):
    physician.id = next_id()
    physicians_list.append(physician)
    return physician

# modificar médico
@router.put("/{id}", response_model=Physician)
def modify_physician(id: int, physician: Physician):
    for index, saved_physician in enumerate(physicians_list):
        if saved_physician.id == id:
            physician.id = id
            physicians_list[index] = physician
            return physician
    raise HTTPException(status_code=404, detail="Physician not found")

# eliminar médico
@router.delete("/{id}")
def remove_physician(id: int):
    for saved_physician in physicians_list:
        if saved_physician.id == id:
            physicians_list.remove(saved_physician)
            return{}
    raise HTTPException(status_code=404, detail="Physician not found")

# obtiene el siguiente id
def next_id():
    # encuentra el id más grande en la lista y devuelve el siguiente valor
    return max([physician.id for physician in physicians_list], default=0) + 1
