# Escribe un programa que lea 10 números por teclado 
# y que luego los muestre ordenados de mayor a menor.
# Creamos lista vacía
numbers = []

# Pedimos 10 números
for _ in range(10):
    # Leemos número
    num = float(input("Enter a number: "))
    # Lo añadimos a la lista
    numbers.append(num)

# Ordenamos de mayor a menor
numbers.sort(reverse=True)

# Mostramos lista ordenada
print(numbers)
