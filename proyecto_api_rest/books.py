from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# entidad libro
class Book(BaseModel):
    id:int
    precio:float
    isbn:str
    titulo:str
    num_paginas:int
    tematica:str
    id_editorial:int

# lista de libros
books_list = [
    Book(id=1, precio=20.99, isbn="978-84-313-2087-2", titulo="Don Quijote de la Mancha", num_paginas=1000, tematica="Novela", id_editorial=1),
    Book(id=2, precio=15.50, isbn="978-84-08-19272-9", titulo="Cien años de soledad", num_paginas=420, tematica="Realismo mágico", id_editorial=2),
    Book(id=3, precio=12.00, isbn="978-84-670-3499-0", titulo="El hobbit", num_paginas=350, tematica="Fantasía", id_editorial=3),
]

@app.get("/books")
def books():
    return books_list

@app.get("/books/{id_book}")
def get_book(id_book: int):
    books = [book for book in books_list
                   if book.id==id_book]
    if len(books) != 0:
        return books[0] 
    else:
        {"error" : "Book not found"}

@app.get("/books/isbn/{isbn_book}")
def get_book_by_isbn(isbn_book: str):
    books = [book for book in books_list
                   if book.isbn==isbn_book]
    if len(books) != 0:
        return books[0] 
    else:
        {"error" : "Book not found"}
        
@app.get("/books/titulo/{titulo_book}")
def get_book_by_titulo(titulo_book: str):
    books = [book for book in books_list
                   if book.titulo==titulo_book]
    if len(books) != 0:
        return books[0] 
    else:
        {"error" : "Book not found"}


@app.post ("/books", status_code=201, response_model=Book)
def add_book(book: Book):
    # Calculamos el siguiente id y se lo 
    # machacamos al libro recibido por parámetro
    book.id = next_id()
    
    # Añadimos el libro a la lista
    books_list.append(book)

    # Devolvemos el libro añadido
    return book

def next_id():
    return (max(books_list, key=id).id+1)

@app.put("/books/{id}")
def modify_book(id:int, book:Book):
    for index, saved_book in enumerate(books_list):
        if saved_book.id == id:
            book.id = id
            books_list[index] = book
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{isbn}")
def modify_book(isbn:int, book:Book):
    for index, saved_book in enumerate(books_list):
        if saved_book.id == id:
            book.id = id
            books_list[index] = book
            return book

    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{id}")
def remove_book(id: int):
    for saved_book in books_list:
        if saved_book.id == id:
            books_list.remove(saved_book)
            return {}
    raise HTTPException(status_code=404, detail="Book not found")