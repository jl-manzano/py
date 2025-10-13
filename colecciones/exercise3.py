# Realiza un programa que pida 8 números enteros 
# y los almacene en una lista. A continuación, 
# recorrerá esa tabla y mostrará esos números junto 
# con la palabra “par” o “impar” según proceda.
# Creamos lista vacía
numbers = []

# Pedimos 8 números enteros
for _ in range(8):
    # Leemos número
    num = int(input("Enter an integer number: "))
    # Lo guardamos en la lista
    numbers.append(num)

# Recorremos lista
for num in numbers:
    # Si es par
    if num % 2 == 0:
        # Mostramos que es par
        print(f"{num} is even")
    else:
        # Mostramos que es impar
        print(f"{num} is odd")

#for i in range(len(numbers)):
 #   if numbers[i] % 2 == 0:
  #      print(f"{numbers[i]} is even")
  #  else:
   #     print(f"{numbers[i]} is odd")