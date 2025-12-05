# Función para transformar un solo médico en formato diccionario
def physician_schema(physician) -> dict:
    return {
        "id": str(physician.id) if physician.id else None,
        "name": physician.name,
        "surname": physician.surname,
        "ncolegiado": physician.ncolegiado,
        "speciality": physician.speciality
    }

# Función para transformar una lista de médicos
def physicians_schema(physicians) -> list:
    return [physician_schema(physician) for physician in physicians]