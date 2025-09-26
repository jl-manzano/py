# Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.
n = int(input("Introduce el número hasta el que desea contar: "))
for i in range(1, n + 1):
    print(i)
    