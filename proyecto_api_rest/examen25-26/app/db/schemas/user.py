# Función para transformar un solo user en formato diccionario
def user_schema(user) -> dict:
    return {"username": str(user["_username"]),
            "fullname": user["fullname"],
            "email": user["email"],
            "disabled": user["disabled"],
            "password": user["password"],
}

# Función para transformar una lista de users
def users_schema(users) -> list:
    return [user_schema(user) for user in users]