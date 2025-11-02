from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import medico, paciente

app = FastAPI()

app.include_router(medico.router)
app.include_router(paciente.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"hello" : "world"}