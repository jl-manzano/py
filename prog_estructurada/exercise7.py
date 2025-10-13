# Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
# Pedimos número
num = int(input("Introduce un número entero positivo: "))

# Asumimos que es primo
es_primo = True

# Empezamos en 2
div = 2

# Comprobamos casos menores o iguales a 1
if num <= 1:
    # No es primo
    print(f"{num} no es un número primo.")
else:
    # Recorremos divisores
    while es_primo and div * div <= num:
        # Si divide exacto
        if num % div == 0:
            # No es primo
            es_primo = False
        # Pasamos al siguiente divisor
        div += 1

# Mostramos resultado
if es_primo:
    # Es primo
    print(f"{num} es un número primo.")
else:
    # No es primo
    print(f"{num} no es un número primo.")
