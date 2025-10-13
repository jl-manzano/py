# Crea un programa que pida diez números reales 
# por teclado, los almacene en una lista, y luego lo 
# recorra para averiguar el máximo y mínimo y 
# mostrarlos por pantalla.
# Creamos lista vacía
numbers = []

# Pedimos 10 números reales
for _ in range(10):
    # Leemos número
    num = float(input("Enter a real number: "))
    # Lo añadimos a la lista
    numbers.append(num)

# Mostramos máximo
print(f"Maximum number: {max(numbers)}")
# Mostramos mínimo
print(f"Minimun number: {min(numbers)}")
