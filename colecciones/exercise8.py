# Diseña un programa que registre las ventas de una 
# tienda en un diccionario, donde las claves son los 
# nombres de los productos y los valores son las 
# cantidades vendidas. El programa debe permitir al 
# usuario agregar nuevas ventas y calcular el total de 
# ventas para un producto específico. 
# Implementa un menú con ambas opciones. 
# Creamos diccionario de ventas
sales = {}

# Función para añadir venta
def add_sale(product, quantity):
    if product in sales:
        sales[product] += quantity
        print(f"Added {quantity} to {product}.")
    else:
        sales[product] = quantity
        print(f"Product {product} added with quantity {quantity}.")

# Función para mostrar total
def total_sales(product):
    if product in sales:
        print(f"Total sales for {product}: {sales[product]}")
    else:
        print(f"No sales recorded for {product}.")

# Función para mostrar menú
def display_menu():
    print("1. Add Sale")
    print("2. Total Sales for a Product")
    print("3. Exit")

# Variable de control
option = 0

# Bucle principal
while option != 3:
    display_menu()
    option = int(input("Choose an option: "))
    match option:
        case 1:
            product = input("Enter product name: ")
            quantity = int(input("Enter quantity sold: "))
            add_sale(product, quantity)
        case 2:
            product = input("Enter product name to check total sales: ")
            total_sales(product)
        case 3:
            print("Exiting the program.")
        case _:
            print("Invalid option. Please try again.")