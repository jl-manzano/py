from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/publishers", tags=["publishers"])

# entidad editorial
class Publisher(BaseModel):
    id: int
    cif: str
    razonSocial: str
    direccion: str
    web: str
    correo: str
    telefono: str

# lista de editoriales
publishers_list = [
    Publisher(id=1, cif="A12345678", razonSocial="Grupo Santillana", direccion="Avenida de la Universidad, 24, 28232 Las Rozas, Madrid, España", web="www.santillana.com", correo="santillana@santillana.es", telefono="+34 91 714 81 00"),
    Publisher(id=2, cif="B23456789", razonSocial="Editorial Planeta", direccion="Gran Vía de les Corts Catalanes, 614, 08007 Barcelona, España", web="https://www.planetadelibros.com", correo="planeta@planeta.es", telefono="+34 93 270 12 00"),
    Publisher(id=3, cif="C34567890", razonSocial="Penguin Random House", direccion="Avenida de la Vega, 15, 28108 Alcobendas, Madrid, España", web="https://www.penguinrandomhousegrupoeditorial.com", correo="informacion@penguinrandomhouse.es", telefono="+34 91 559 75 00"),
]

# obtener todas las editoriales
@router.get("/")
def get_publishers():
    return publishers_list

# buscar por id
@router.get("/{id_publisher}")
def get_publisher(id_publisher: int):
    publishers = [p for p in publishers_list if p.id == id_publisher]
    if publishers:
        return publishers[0]
    else:
        raise HTTPException(status_code=404, detail="Publisher not found")

# buscar por cif
@router.get("/cif/{cif_publisher}")
def get_publisher_by_cif(cif_publisher: str):
    publishers = [p for p in publishers_list if p.cif.lower() == cif_publisher.lower()]
    if publishers:
        return publishers[0]
    else:
        raise HTTPException(status_code=404, detail="Publisher not found")

# buscar por razón social
@router.get("/razon_social/{razon_social}")
def get_publisher_by_razon_social(razon_social: str):
    publishers = [p for p in publishers_list if p.razonSocial.lower() == razon_social.lower()]
    if publishers:
        return publishers[0]
    else:
        raise HTTPException(status_code=404, detail="Publisher not found")

# añadir una editorial
@router.post("/", status_code=201)
def add_publisher(publisher: Publisher):
    publisher.id = next_id()
    publishers_list.append(publisher)
    return publisher

# modificar editorial
@router.put("/{id}", response_model=Publisher)
def modify_publisher(id: int, publisher: Publisher):
    for index, saved_publisher in enumerate(publishers_list):
        if saved_publisher.id == id:
            publisher.id = id
            publishers_list[index] = publisher
            return publisher
    raise HTTPException(status_code=404, detail="Publisher not found")

# eliminar editorial
@router.delete("/{id}")
def remove_publisher(id: int):
    for saved_publisher in publishers_list:
        if saved_publisher.id == id:
            publishers_list.remove(saved_publisher)
            return {}
    raise HTTPException(status_code=404, detail="Publisher not found")

# obtiene el siguiente id
def next_id():
    # encuentra el id más grande en la lista y devuelve el siguiente valor
    return max([publisher.id for publisher in publishers_list], default=0) + 1