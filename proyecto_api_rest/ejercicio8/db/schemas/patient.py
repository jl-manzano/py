# Función para transformar un solo paciente en formato diccionario
def patient_schema(patient) -> dict:
    return {
        "id": str(patient.id) if patient.id else None,
        "dni": patient.dni,
        "apellidos": patient.apellidos,
        "nombre": patient.nombre,
        "segsocial": patient.segsocial,
        "fnacimiento": patient.fnacimiento,
        "id_medico": patient.id_medico
    }

# Función para transformar una lista de pacientes
def patients_schema(patients) -> list:
    return [patient_schema(patient) for patient in patients]