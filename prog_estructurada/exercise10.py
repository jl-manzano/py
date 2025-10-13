# Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.
# Definimos función
def maximo(num1, num2):
    # Si el primero es mayor
    if num1 > num2:
        # Guardamos num1
        maximo = num1
    else:
        # Guardamos num2
        maximo = num2
    # Devolvemos resultado
    return maximo

# Función principal
def main():
    # Pedimos primer número
    num1 = int(input("Introduce el primer número: "))
    # Pedimos segundo número
    num2 = int(input("Introduce el segundo número: "))
    # Mostramos resultado
    print(f"El máximo entre {num1} y {num2} es {maximo(num1, num2)}")

# Ejecutamos main
if __name__ == "__main__":
    # Llamamos a main
    main()
