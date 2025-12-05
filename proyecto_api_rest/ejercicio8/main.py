from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import paciente, auth_users, medico, medico_db, paciente_db

app = FastAPI()

app.include_router(medico.router)
app.include_router(paciente.router)
app.include_router(auth_users.router)
app.include_router(paciente_db.router)
app.include_router(medico_db.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"hello" : "world"}