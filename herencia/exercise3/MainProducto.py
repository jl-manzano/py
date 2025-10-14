# Importamos clases
from Producto import Producto
from Perecedero import Perecedero
from NoPerecedero import NoPerecedero

# Función principal
def main():
    # Creamos productos
    producto1 = Producto("Producto genérico", 100)
    producto2 = Perecedero("Leche", 1.5, 2)
    producto3 = NoPerecedero("Arroz", 0.8, "Alimento")

    # Mostramos productos
    print(producto1)
    print(producto2)
    print(producto3)

    # Lista de productos
    productos = [producto1, producto2, producto3]

    # Ordenamos por precio
    productos.sort()

    # Mostramos precios por 5 unidades
    for prod in productos:
        print(f"{prod.name}: Precio por 5 unidades = {prod.calculate_price(5)}€")

    # Mostramos ordenados
    print("\nProductos ordenados por precio:")
    for prod in productos:
        print(prod)

# Ejecutamos main
if __name__ == "__main__":
    main()