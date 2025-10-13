# Importamos clase Articulo
from Articulo import Articulo

# Creamos varios artículos
art1 = Articulo("Laptop", 1000, 10)
art2 = Articulo("Smartphone", 500, 20)
art3 = Articulo("Tablet", 300, 15)
art4 = Articulo("Laptop", 1200, 5)

# Mostramos todos
print(art1)
print(art2)
print(art3)
print(art4)

# Mostramos PVPs
print("PVP of art1:", art1.getPVP())
print("PVP of art2 with 10% discount:", art2.getPVPDescuento(10))

# Intentamos vender
if art1.vender(5):
    print("Sale successful")
else:
    print("Not enough stock for sale")

def main():
    art1 = Articulo("Laptop", 1000, 10)
    art2 = Articulo("Smartphone", 500, 20)
    art3 = Articulo("Tablet", 300, 15)
    art4 = Articulo("Laptop", 1200, 5)
    print(art1)
    print(art2)
    print(art3)
    print(art4)

    print("PVP of art1:", art1.getPVP())
    print("PVP of art2 with 10% discount:", art2.getPVPDescuento(10))

    if art1.vender(5):
        print("Sale successful")
    else:
        print("Not enough stock for sale")

    if art2.vender(25):
        print("Sale successful")
    else:
        print("Not enough stock for sale")

# Almacenamos en art3
art3.almacenar(10)

# Mostramos después de cambios
print(art1)
print(art2)
print(art3)

# Comparamos si art1 y art4 son iguales
if art1 == art4:
    print("art1 and art4 are the same article")
else:
    print("art1 and art4 are different articles")

# Ordenamos artículos por nombre
articles = [art1, art2, art3, art4]
articles.sort()
print("Articles sorted by name:")
for art in articles:
    print(art)

    art3.almacenar(10)
    print(art1)
    print(art2)
    print(art3)

    if art1 == art4:
        print("art1 and art4 are the same article")
    else:
        print("art1 and art4 are different articles")

    articles = [art1, art2, art3, art4]
    articles.sort()
    print("Articles sorted by name:")
    for art in articles:
        print(art)

main()
