# Crea un programa que permita al usuario agregar, 
# eliminar y buscar contactos en una libreta de 
# direcciones implementada como un diccionario. 
# La clave del diccionario será el nombre del contacto 
# y el valor, su número de teléfono. 
# Crea un menú para las distintas opciones e implementa
# una función para cada opción.
agenda = {}

def add_contact(name, phone):
    agenda[name] = phone
    print(f"Contact {name} added with phone number {phone}.")

def delete_contact(name):
    if name in agenda:
        del agenda[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def search_contact(name):
    if name in agenda:
        print(f"Contact {name}: {agenda[name]}")
    else:
        print(f"Contact {name} not found.")

def display_menu():
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Exit")

option = 0
while option != 4:
    display_menu()
    option = int(input("Choose an option: "))
    match option:
        case 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        case 2:
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        case 3:
            name = input("Enter contact name to search: ")
            search_contact(name)
        case 4:
            print("Exiting the program.")
        case _:
            print("Invalid option. Please try again.")