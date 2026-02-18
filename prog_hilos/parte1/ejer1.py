import threading
import random
import time

class Trabajador(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            tiempo = random.randint(1, 10)
            time.sleep(tiempo)
            print(f"Soy {self.name} y he terminado de trabajar")


if __name__ == "__main__":
    nombres = ["Ana", "Luis", "María", "Pedro", "Sofía"]

    hilos = []
    for nombre in nombres:
        hilo = Trabajador(nombre)
        hilo.setDaemon(True)  # El programa termina si solo quedan hilos demonio
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    # Dejamos que los hilos trabajen durante 30 segundos
    time.sleep(30)
    print("\n--- Fin de la simulación ---")