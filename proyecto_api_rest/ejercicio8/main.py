from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import paciente, auth_users, medico

app = FastAPI()

app.include_router(medico.router)
app.include_router(paciente.router)
app.include_router(auth_users.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"hello" : "world"}