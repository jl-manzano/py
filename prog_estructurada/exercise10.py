# Diseñar una función que recibe como parámetros dos números enteros y devuelve el máximo de ambos.
def maximo(num1, num2):
    if num1 > num2:
        maximo = num1
    else:
        maximo = num2
    return maximo

def main():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    print(f"El máximo entre {num1} y {num2} es {maximo(num1, num2)}")

if __name__ == "__main__":
    main()