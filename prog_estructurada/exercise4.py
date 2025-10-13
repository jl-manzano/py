# Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente). 
# Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, 
# según sea mayor o menor con respecto al número secreto. El proceso termina cuando el usuario acierta 
# o cuando se rinde (introduciendo un -1).
# Importamos random
import random

# Generamos número secreto
rand = random.randint(1, 100)

# Pedimos intento del usuario
numero_usuario = int(input("Adivina el número (o -1 para rendirte): "))

# Mientras no acierte ni se rinda
while numero_usuario != rand and numero_usuario != -1:
    # Si el número es menor
    if numero_usuario < rand:
        # Indicamos que es mayor
        print("El número secreto es mayor.")
    else:
        # Indicamos que es menor
        print("El número secreto es menor.")
    # Pedimos nuevo intento
    numero_usuario = int(input("Adivina el número (o -1 para rendirte): "))

# Si acierta
if numero_usuario == rand:
    # Mensaje de acierto
    print("¡Felicidades! Has acertado el número secreto.")
else:
    # Mensaje de rendición
    print(f"Te has rendido. El número secreto era {rand}.")
