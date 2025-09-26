# Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. 
# Desde el método main() lee los dos números enteros, los cuales deben introducirlos el usuario, 
# y pásalos como parámetros de entrada de la función.
def mostrar_numeros_entre(num1, num2):
    if num1 < num2:
        for i in range(num1, num2 + 1):
            print(i)
    else:
        for i in range(num2, num1 + 1):
            print(i)

def main():
    num1 = int(input("Introduce el primer número:"))
    num2 = int(input("Introduce el segundo número:"))
    mostrar_numeros_entre(num1, num2)

if __name__ == "__main__":
    main()