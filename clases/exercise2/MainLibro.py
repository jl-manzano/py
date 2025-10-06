from Libro import Libro

def main():
    book1 = Libro("1984", "George Orwell", 5, 2)
    book2 = Libro("Brave New World", "Aldous Huxley", 3, 1)
    book3 = Libro("1984", "George Orwell", 5, 2)

    print(book1)
    print(book2)
    print(book3)

    if book1.prestamo():
        print("Loan successful")
    else:
        print("No copies available for loan")

    if book2.devolucion():
        print("Return successful")
    else:
        print("No copies were loaned out to return")

    if book1 == book3:
        print("The books are the same")
    else:
        print("The books are different")

    if book1 < book2:
        print("Book 1's author comes before Book 2's author")
    else:
        print("Book 1's author comes after or is the same as Book 2's author")

    books = [book1, book2, book3]
    books.sort()
    print("Books sorted by author:")
    for book in books:
        print(book)

if __name__ == "__main__":
    main()