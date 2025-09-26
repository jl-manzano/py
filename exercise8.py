# Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
#   *
#  * *
# * * *
#* * * *
num = int(input("Introduce la altura y base del triángulo: "))
for i in range(1, num + 1):
    print(" " * (num - i) + "* " * i)