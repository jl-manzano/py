# Crea un programa que cree una lista de enteros de 
# tamaño 100 y lo rellene con valores enteros aleatorios 
# entre 1 y 10 (utiliza 1 + Math.random()*10). 
# Luego pedirá un valor N y mostrará cuántas veces 
# aparece N. 
import random
numbers = []
for _ in range(100):
    numbers.append(random.randint(1, 10))
# print(numbers)
n = int(input("Enter a number between 1 and 10 to count its ocurrences: "))
count = numbers.count(n)
print(f"The number {n} appears {count} times in the list.")