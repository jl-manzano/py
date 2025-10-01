# Escribe un programa que lea 10 números por teclado 
# y que luego los muestre ordenados de mayor a menor.
numbers = []
for _ in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

numbers.sort(reverse=True)
print(numbers)
