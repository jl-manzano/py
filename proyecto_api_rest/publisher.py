from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# entidad editorial
class Publisher(BaseModel):
    id:int
    cif:str
    razonSocial:str
    direccion:str
    web:str
    correo:str
    telefono:str

# lista de editoriales
publishers_list = [
    Publisher(id=1, cif="A12345678", razonSocial="Grupo Santillana", direccion="Avenida de la Universidad, 24, 28232 Las Rozas, Madrid, España", web="www.santillana.com", correo="santillana@santillana.es", telefono="+34 91 714 81 00"),
    Publisher(id=2, cif="B23456789", razonSocial="Editorial Planeta", direccion="Gran Vía de les Corts Catalanes, 614, 08007 Barcelona, España", web="https://www.planetadelibros.com", correo="planeta@planeta.es", telefono="+34 93 270 12 00"),
    Publisher(id=3, cif="C34567890", razonSocial="Penguin Random House", direccion="Avenida de la Vega, 15, 28108 Alcobendas, Madrid, España", web="https://www.penguinrandomhousegrupoeditorial.com", correo="informacion@penguinrandomhouse.es", telefono="+34 91 559 75 00"),
]

@app.get("/publishers")
def publishers():
    return publishers_list

@app.get("/publishers/{id_publisher}")
def get_publisher(id_publisher: int):
    publishers = [publisher for publisher in publishers_list
                   if publisher.id==id_publisher]
    if len(publishers) != 0:
        return publishers[0] 
    else:
        {"error" : "Publisher not found"}

@app.get("/publishers/cif/{cif_publisher}")
def get_publisher_by_cif(cif_publisher: str):
    publishers = [publisher for publisher in publishers_list
                   if publisher.cif.lower()==cif_publisher.lower()]
    if len(publishers) != 0:
        return publishers[0] 
    else:
        {"error" : "Publisher not found"}

@app.get("/publishers/razon_social/{razon_social}")
def get_publisher_by_razon_social(razon_social: str):
    publishers = [publisher for publisher in publishers_list
                   if publisher.razonSocial.lower()==razon_social.lower()]
    if len(publishers) != 0:
        return publishers[0] 
    else:
        {"error" : "Publisher not found"}

@app.post ("/publishers", status_code=201, response_model=Publisher)
def add_Publisher(publisher: Publisher):
    # Calculamos el siguiente id y se lo 
    # machacamos a la editorial recibida por parámetro
    publisher.id = next_id()
    
    # Añadimos la editorial a la lista
    publishers_list.append(publisher)

    # Devolvemos la editorial añadido
    return publisher

def next_id():
    return (max(publishers_list, key=id).id+1)

@app.put("/publishers/{id}")
def modify_publisher(id:int, publisher:Publisher):
    for index, saved_publisher in enumerate(publishers_list):
        if saved_publisher.id == id:
            publisher.id = id
            publishers_list[index] = publisher
            return publisher

    raise HTTPException(status_code=404, detail="Publisher not found")

@app.delete("/publishers/{id}")
def remove_publisher(id: int):
    for saved_publisher in publishers_list:
        if saved_publisher.id == id:
            publishers_list.remove(saved_publisher)
            return {}
    raise HTTPException(status_code=404, detail="Publisher not found")