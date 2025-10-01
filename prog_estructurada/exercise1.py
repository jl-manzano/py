# Diseñar una aplicación que solicite al usuario un número e indique si es par o impar.
numero = input("Introduce un número: ")
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
