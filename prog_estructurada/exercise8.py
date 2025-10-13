# Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
#   *
#  * *
# * * *
#* * * *
# Pedimos tamaño del triángulo
num = int(input("Introduce la altura y base del triángulo: "))

# Recorremos filas
for i in range(1, num + 1):
    # Imprimimos espacios y asteriscos
    print(" " * (num - i) + "* " * i)
