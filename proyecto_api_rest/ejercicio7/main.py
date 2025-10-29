from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import books, publisher

app = FastAPI()

app.include_router(books.router)
app.include_router(publisher.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"hello" : "world"}