# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.
# Pide un número y dice si es par o impar
numero = int(input("Introduce un número: "))

# Comprueba si es par
if numero % 2 == 0:
    print(f"El número {numero} es par.")
# Si no, es impar
else:
    print(f"El número {numero} es impar.")