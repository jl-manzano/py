# Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
# Pedimos número
num = int(input("Introduce un número para calcular su factorial: "))

# Inicializamos factorial
factorial = 1

# Recorremos del 1 al número
for i in range(1, num + 1):
    # Multiplicamos acumulando
    factorial *= i

# Mostramos resultado
print(f"El factorial de {num} es {factorial}.")
