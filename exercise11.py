# Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa 
# como parámetro de entrada corresponde con una vocal.
def es_vocal(c):
    return c.lower() in 'aeiou'

def main():
    c = input("Introduce un carácter: ")

    if es_vocal(c):
        print(f"El carácter '{c}' es una vocal.")
    else:
        print(f"El carácter '{c}' no es una vocal.")

if __name__ == "__main__":
    main()