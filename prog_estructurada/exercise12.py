# Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) 
# y qué operación se desea realizar con ellos. 
# Las operaciones disponibles son sumar, restar, multiplicar o dividir. 
# Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división. 
# La función devolverá el resultado de la operación mediante un número real.
def calculadora(o1, o2, oper):
    if oper == 1:
        res =  o1 + o2
    elif oper == 2:
        res =  o1 - o2
    elif oper == 3:
        res =  o1 * o2
    elif oper == 4:
        if o2 != 0:
            res =  o1 / o2
        else:
            res = "Error: División por cero"
    else:
        res = "Operación no válida"
    return res

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    operacion = int(input("Elige una operación (1-4): "))
    resultado = calculadora(num1, num2, operacion)
    print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()    