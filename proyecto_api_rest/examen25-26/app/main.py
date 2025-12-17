from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import alumnos, auth_users, colegios

app = FastAPI()

app.include_router(alumnos.router)
app.include_router(colegios.router)
app.include_router(auth_users.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"hello" : "world"}