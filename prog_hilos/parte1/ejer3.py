import threading
import random

class Adivinador(threading.Thread):
    # Número a adivinar (compartido por todos los hilos)
    numero_secreto = random.randint(0, 100)
    # Variable que indica si alguien ya ha acertado
    alguien_acerto = False

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        intentos = 0
        print(f"Hilo {self.name} comienza a buscar el número...")

        while True:
            # El hilo genera un número aleatorio
            intento = random.randint(0, 100)
            intentos += 1

            # Comprueba si ha acertado
            if intento == Adivinador.numero_secreto:
                Adivinador.alguien_acerto = True
                print(f"¡Hilo {self.name} ha acertado el número {intento} en {intentos} intentos!")
                return

            # Comprueba si otro hilo ya ha acertado
            if Adivinador.alguien_acerto:
                print(f"Hilo {self.name} se detiene porque otro hilo ya acertó (llevaba {intentos} intentos).")
                return

            # Si nadie ha acertado, sigue buscando


if __name__ == "__main__":
    print(f"[DEBUG] Número secreto: {Adivinador.numero_secreto}")

    hilos = []
    for i in range(10):
        hilo = Adivinador(str(i))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\n--- Todos los hilos han terminado ---")