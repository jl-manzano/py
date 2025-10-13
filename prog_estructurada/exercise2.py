# Pedir dos números y mostrarlos ordenados de menor a mayor.
# Pido el primer número y lo convierto a entero.
num1 = int(input("Introduce el primer número: "))

# Pido el segundo número y también lo convierto a entero.
num2 = int(input("Introduce el segundo número: "))

# Compruebo cuál de los dos es menor.
if num1 < num2:
    # Si el primero es menor, los muestro en el mismo orden.
    print(f"Números ordenados: {num1}, {num2}")
else:
    # Si no, los muestro al revés.
    print(f"Números ordenados: {num2}, {num1}")