from datetime import *
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException

import jwt
from jwt import PyJWTError
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

# Definimos el algoritmo de encriptación
ALGORITHM = "HS256"

# Duración del token
ACCESS_TOKEN_EXPIRE_MINUTES = 5

# Clave que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "ecc4dbc5fc484eab20f2eb1c60a8e56f423f45ae7d96c7254d75bf2b5ae6beea"

# Objeto que se utilizará para el cálculo del hash y la verificación de las contraseñas
password_hash = PasswordHash.recommended()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "elenarg" : {
        "username" : "elenarg",
        "fullname" : "Elena Rivero",
        "email" : "elenarg@prueba.es",
        "disabled" : False,
        "password" : "123456"
    } 
}

@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user.model_dump()
        return user
    else:
        raise HTTPException(status_code = 409, detail="User already exists")
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    #print(user_db)
    if user_db:
        # si usuario existe en bd
        # comprobamos las contraseñas
        # creamos el usuario de tipo UserDB
        user = UserDB(**users_db[form.username])
        print(user)
        try:
            if password_hash.verify(form.password, user.password):
                expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = { "sub": user.username, "exp": expire}
                # generamos token
                token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
                return { "access_token":token, "token_type":"bearer"}
        except:
            raise HTTPException(status_code=400, detail="Error en la autenticación")
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

async def authentication(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM).get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Credenciales de autenticación inválidas",
                                headers={"WWW-Authenticate" : "Bearer"})
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate" : "Bearer"})
    
    user = User(**users_db[username])

    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuario inactivo")
    
    return user