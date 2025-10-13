# Importamos Gato y Perro
from Gato import Gato
from Perro import Perro

# Función principal
def main():
    # Creamos gato
    gato = Gato("Michi", 4)
    # Creamos perro
    perro = Perro("Firulais", 4)
    # Mostramos gato
    print(gato)
    # Mostramos perro
    print(perro)

# Ejecutamos si es main
if __name__ == "__main__":
    main()