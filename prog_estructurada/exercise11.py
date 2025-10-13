# Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa 
# como parámetro de entrada corresponde con una vocal.
# Función que comprueba si es vocal
def es_vocal(c):
    return c.lower() in 'aeiou'

# Función principal
def main():
    # Pedimos carácter
    c = input("Introduce un carácter: ")

    # Comprobamos si es vocal
    if es_vocal(c):
        print(f"El carácter '{c}' es una vocal.")
    else:
        print(f"El carácter '{c}' no es una vocal.")

# Ejecutamos main
if __name__ == "__main__":
    main()
