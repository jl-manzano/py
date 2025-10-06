from Producto import Producto
from Perecedero import Perecedero
from NoPerecedero import NoPerecedero

def main():
    producto1 = Producto("Producto genérico", 100)
    producto2 = Perecedero("Leche", 1.5, 2)
    producto3 = NoPerecedero("Arroz", 0.8, "Alimento")

    print(producto1)
    print(producto2)
    print(producto3)

    productos = [producto1, producto2, producto3]
    productos.sort()

    for prod in productos:
        print(f"{prod.name}: Precio por 5 unidades = {prod.calculate_price(5)}€")

    print("\nProductos ordenados por precio:")
    for prod in productos:
        print(prod)

if __name__ == "__main__":
    main()