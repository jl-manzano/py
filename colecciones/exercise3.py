# Realiza un programa que pida 8 números enteros 
# y los almacene en una lista. A continuación, 
# recorrerá esa tabla y mostrará esos números junto 
# con la palabra “par” o “impar” según proceda.
numbers = []
for _ in range(8):
    num = int(input("Enter a integer number: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#for i in range(len(numbers)):
 #   if numbers[i] % 2 == 0:
  #      print(f"{numbers[i]} is even")
  #  else:
   #     print(f"{numbers[i]} is odd")