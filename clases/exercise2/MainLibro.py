# Importamos clase Libro
from Libro import Libro

# Función principal
def main():
    # Creamos libros
    book1 = Libro("1984", "George Orwell", 5, 2)
    book2 = Libro("Brave New World", "Aldous Huxley", 3, 1)
    book3 = Libro("1984", "George Orwell", 5, 2)

    # Mostramos libros
    print(book1)
    print(book2)
    print(book3)

    # Probamos préstamo
    if book1.prestamo():
        print("Loan successful")
    else:
        print("No copies available for loan")

    # Probamos devolución
    if book2.devolucion():
        print("Return successful")
    else:
        print("No copies were loaned out to return")

    # Comparación
    if book1 == book3:
        print("The books are the same")
    else:
        print("The books are different")

    # Comparación por autor
    if book1 < book2:
        print("Book 1's author comes before Book 2's author")
    else:
        print("Book 1's author comes after or is the same as Book 2's author")

    # Lista y ordenación
    books = [book1, book2, book3]
    books.sort()
    print("Books sorted by author:")
    for book in books:
        print(book)