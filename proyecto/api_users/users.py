from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    id:int
    name:str
    surname:str
    age: int

# la siguiente lista pretende simular una base de datos para probar nuestra API
users_list = [User (id = 1, name = "Paco", surname="Pérez", age=30),
    User (id = 2, name = "Maria", surname="Martínez", age=20),
    User (id = 3, name = "Lucía", surname="Rodríquez", age=40)]

@app.get("/users")
def users():
    return users_list

@app.get("/users/{id_user}")
def get_user(id_user: int):
    users = [user for user in users_list 
             if user.id==id_user]

    return users[0] if len(users) != 0 else {"error" : "User not found"}

@app.post ("/users", status_code=201, response_model=User)
def add_user(user: User):
    # Calculamos el siguiente id y se lo 
    # machacamos al usuario recibido por parámetro
    user.id = next_id()
    
    # Añadimos el usuario a la lista
    users_list.append(user)

    # Devolvemos el usuario añadido
    return user

def next_id():
    return (max(users_list, key=id).id+1)

@app.put("/users/{id}")
def modify_user(id:int, user:User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            user.id = id
            users_list[index] = user
            return user

    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{id}")
def remove_user(id: int):
    for saved_user in users_list:
        if saved_user.id == id:
            users_list.remove(saved_user)
            return {}
    raise HTTPException(status_code=404, detail="User not found")

def search_user(id: int):
    # buscamos usuario por id en la lista
    # devuelve una lista vacía si no encuentra nada
    # devuelve una lista con el usuario encontrado
    users = [user for user in users_list if user.id == id]

    # devolvemos la primera posición de la lista si encuentra algo
    # devolvemos un diccionario con el error si no encuentra usuario
    if not users:
        raise HTTPException(status_code=404, detail="User not found")

    return users[0]

