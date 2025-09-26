# Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
# Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
# antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.
suma = 0
numero = int(input("Introduce un número entero positivo o un número negativo para terminar: "))
while numero >= 0:
    suma += numero
    numero = int(input("Introduce otro número entero positivo o un número negativo para terminar: "))
    
print(f"Suma: {suma}")

