# Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. 
# Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, 
# y pásalos como parámetros de entrada de la función.
# Definimos función
def mostrar_numeros_entre(num1, num2):
    # Si el primero es menor
    if num1 < num2:
        # Recorremos hacia arriba
        for i in range(num1, num2 + 1):
            # Mostramos número
            print(i)
    else:
        # Recorremos hacia abajo
        for i in range(num2, num1 + 1):
            # Mostramos número
            print(i)

# Función principal
def main():
    # Pedimos primer número
    num1 = int(input("Introduce el primer número: "))
    # Pedimos segundo número
    num2 = int(input("Introduce el segundo número: "))
    # Llamamos a la función
    mostrar_numeros_entre(num1, num2)

# Ejecutamos programa
if __name__ == "__main__":
    # Llamamos a main
    main()
