# Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
# Cuando el usuario no quiera insertar más números, introducirá un número negativo y el algoritmo, 
# antes de acabar, mostrará la suma de los números positivos introducidos por el usuario.
# Inicializamos suma
suma = 0

# Pedimos primer número
numero = int(input("Introduce un número entero positivo o negativo para terminar: "))

# Bucle mientras sea positivo
while numero >= 0:
    # Sumamos número
    suma += numero
    # Pedimos siguiente número
    numero = int(input("Introduce otro número entero positivo o negativo para terminar: "))

# Mostramos suma total
print(f"Suma: {suma}")