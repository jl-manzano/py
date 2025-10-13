# Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.
# Pedimos número final
n = int(input("Introduce el número hasta el que deseas contar: "))

# Recorremos del 1 al número
for i in range(1, n + 1):
    # Mostramos número actual
    print(i)
