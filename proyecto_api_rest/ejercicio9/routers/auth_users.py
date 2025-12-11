from datetime import *
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException

import jwt
from jwt.exceptions import PyJWTError
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

def search_user_db(username: str):
    if username in users_db:
        return UserDB(users_db[username])

# Esta función será nuestra dependencia
# Lo que pretendemos con esta función es que 
# nos devuelva el usuario a partir del token
# En esta función, nuestra relación de dependencia es el objeto oauth2
async def auth_user(token:str = Depends(oauth2)):    
    # Nos creamos un objeto para almacenar la excepción que vamos a lanzar en varias ocasiones
    exception = HTTPException(status_code=401, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"})
     
    # Como la llamada a get puede lanzar una excepción, la capturamos por si acaso
    try:        
        # Para poder obtener el usuario a partir del token tenemos que desencriptarlo
        # con exactamente las mismas características que para encriptarlo
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")
        # Nos aseguramos de que el usuario no es None
        if username is None:
            # Si es None lanzamos la excepción
            raise HTTPException(status_code=401, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"})       
    except PyJWTError:
        # Si ha fallado algo del proceso de la decodificación o si no ha encontrado la clave "sub"
        # lanzamos una excepción HTTP
        raise HTTPException(status_code=401, 
                            detail="Credenciales de autenticación inválidas", 
                            headers={"WWW-Authenticate" : "Bearer"})
        
    # Si hemos llegado a este punto es que no se ha producido ninguna excepción
    # y tenemos un usuario válido
    user = User(**users_db[username])

    if user.disabled:
        # Si el usuario está deshabilitado lanzamos excepción
        raise HTTPException(status_code=400, 
                            detail="Usuario inactivo")   

    # Retornamos un usuario correcto y habilitado
    return user


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

@router.get("/auth/me")
async def me(user: User = Depends(auth_user)):
    return user