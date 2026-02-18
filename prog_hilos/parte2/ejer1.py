import threading
import random

class Adivinador(threading.Thread):
    numero_secreto = random.randint(0, 100)
    alguien_acerto = False
    # Lock para proteger la sección crítica donde se comprueba y actualiza alguien_acerto
    lock = threading.Lock()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        intentos = 0
        print(f"Hilo {self.name} comienza a buscar el número...")

        while True:
            intento = random.randint(0, 100)
            intentos += 1

            # Sección crítica: comprobamos y modificamos alguien_acerto de forma atómica
            Adivinador.lock.acquire()
            if intento == Adivinador.numero_secreto and not Adivinador.alguien_acerto:
                Adivinador.alguien_acerto = True
                Adivinador.lock.release()
                print(f"¡Hilo {self.name} ha acertado el número {intento} en {intentos} intentos!")
                return
            elif Adivinador.alguien_acerto:
                Adivinador.lock.release()
                print(f"Hilo {self.name} se detiene (llevaba {intentos} intentos).")
                return
            else:
                Adivinador.lock.release()


if __name__ == "__main__":
    print(f"[DEBUG] Número secreto: {Adivinador.numero_secreto}\n")

    hilos = [Adivinador(str(i)) for i in range(10)]

    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    print("\n--- Todos los hilos han terminado ---")