# Crea una lista de enteros de longitud 10 
# que se inicializará con números aleatorios 
# comprendidos entre 1 y 100. 
# Importamos random
import random

# Creamos lista vacía
numbers = []

# Generamos 10 números aleatorios
for _ in range(10):
    # Añadimos número a la lista
    numbers.append(random.randint(1, 100))

# Mostramos la lista
print(numbers)
