# Crea un programa que pida diez números reales 
# por teclado, los almacene en una lista, y luego lo 
# recorra para averiguar el máximo y mínimo y 
# mostrarlos por pantalla.
numbers = []
for _ in range(10):
    num = float(input("Enter a real number: "))
    numbers.append(num)

print(f"Maximum number: {max(numbers)}")
print(f"Minimun number: {min(numbers)}")