# Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
# Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, 
# según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta 
# o cuando se rinde (introduciendo un -1).
import random
rand = random.randint(1, 100)
#print(numero_secreto)
numero_usuario = int(input("Adivina el número secreto entre 1 y 100 (o introduce -1 para rendirte): "))
while (numero_usuario != rand and numero_usuario != -1):
    if (numero_usuario < rand):
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    numero_usuario = int(input("Adivina el número secreto entre 1 y 100 (o introduce -1 para rendirte): "))

if (numero_usuario == rand):
    print("¡Felicidades! Has acertado el número secreto.")
else:
    print(f"Te has rendido. El número secreto era {rand}.")