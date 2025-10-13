# Crea un programa que cree una lista de enteros de 
# tamaño 100 y lo rellene con valores enteros aleatorios 
# entre 1 y 10 (utiliza 1 + Math.random()*10). 
# Luego pedirá un valor N y mostrará cuántas veces 
# aparece N. 
# Importamos random
import random

# Creamos lista vacía
numbers = []

# Generamos 100 números del 1 al 10
for _ in range(100):
    # Añadimos número
    numbers.append(random.randint(1, 10))

# Pedimos número a buscar
n = int(input("Enter a number between 1 and 10 to count its occurrences: "))

# Contamos cuántas veces aparece
count = numbers.count(n)

# Mostramos resultado
print(f"The number {n} appears {count} times in the list.")
