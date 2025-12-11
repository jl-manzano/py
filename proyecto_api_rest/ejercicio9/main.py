from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import empleado, auth_users, tienda, empleado_db, tienda_db

app = FastAPI()

app.include_router(empleado.router)
app.include_router(tienda.router)
app.include_router(auth_users.router)
app.include_router(empleado_db.router)
app.include_router(tienda_db.router)

# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"hello" : "world"}