from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import authentication

router = APIRouter(prefix="/patients", tags=["patients"])

# entidad paciente
class Patient(BaseModel):
    id: int
    dni: str
    apellidos: str
    nombre: str
    segsocial: str
    fnacimiento: str
    id_medico: int

# lista de pacientes (ejemplo)
patients_list = [
    Patient(id=1, dni="12345678A", apellidos="Pérez", nombre="Juan", segsocial="123-45-6789", fnacimiento="1990-01-01", id_medico=1),
    Patient(id=2, dni="23456789B", apellidos="González", nombre="Ana", segsocial="234-56-7890", fnacimiento="1985-05-12", id_medico=2),
    Patient(id=3, dni="34567890C", apellidos="Martínez", nombre="Carlos", segsocial="345-67-8901", fnacimiento="2000-11-23", id_medico=1),
    Patient(id=4, dni="45678901D", apellidos="Sánchez", nombre="María", segsocial="456-78-9012", fnacimiento="1978-07-30", id_medico=3),
]

# obtener todos los pacientes
@router.get("/")
def get_patients():
    return patients_list

# buscar por id
@router.get("/{id_patient}")
def get_patient_by_id(id_patient: int):
    patients = [p for p in patients_list if p.id == id_patient]
    if patients:
        return patients[0]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# buscar por dni
@router.get("/dni/{dni_patient}")
def get_patient_by_dni(dni_patient: str):
    patients = [p for p in patients_list if p.dni == dni_patient]
    if patients:
        return patients[0]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# buscar por segsocial
@router.get("/segsocial/{segsocial_patient}")
def get_patient_by_segsocial(segsocial_patient: str):
    patients = [p for p in patients_list if p.segsocial == segsocial_patient]
    if patients:
        return patients[0]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

# buscar por id_medico (para obtener los pacientes asignados a ese médico)
@router.get("/medico/{id_medico}")
def get_patients_by_medico(id_medico: int):
    patients = [p for p in patients_list if p.id_medico == id_medico]
    if patients:
        return patients
    else:
        raise HTTPException(status_code=404, detail="No patients found for this physician")

# añadir un paciente
@router.post("/", status_code=201)
def add_patient(patient: Patient,  authorized = Depends(authentication)):
    patient.id = next_id()
    patients_list.append(patient)
    return patient

# modificar paciente
@router.put("/{id}", response_model=Patient)
def modify_patient(id: int, patient: Patient):
    for index, saved_patient in enumerate(patients_list):
        if saved_patient.id == id:
            patient.id = id
            patients_list[index] = patient
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

# eliminar paciente
@router.delete("/{id}")
def remove_patient(id: int):
    for saved_patient in patients_list:
        if saved_patient.id == id:
            patients_list.remove(saved_patient)
            return {}
    raise HTTPException(status_code=404, detail="Patient not found")

# obtiene el siguiente id
def next_id():
    # encuentra el id más grande en la lista y devuelve el siguiente valor
    return max([patient.id for patient in patients_list], default=0) + 1