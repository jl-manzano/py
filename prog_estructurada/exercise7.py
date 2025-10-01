# Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
num = int(input("Introduce un número entero positivo: "))
es_primo = True
div = 2
if num <= 1:
    print(f"{num} no es un número primo.")
else:
    while es_primo and div <= num * 0.05:
        if num % div == 0:
            es_primo = False
        div += 1

if (es_primo):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")