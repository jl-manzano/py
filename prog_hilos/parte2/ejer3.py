import threading
import random
import time

class Cliente(threading.Thread):
    # Semáforo: máximo 4 clientes simultáneos
    semaforo = threading.Semaphore(4)

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"Cliente {self.name} llega a la carnicería y espera.")

        Cliente.semaforo.acquire()
        try:
            print(f">>> El cliente {self.name} está siendo atendido.")
            tiempo = random.randint(1, 10)
            time.sleep(tiempo)
            print(f"<<< El cliente {self.name} ha terminado en la carnicería (tardó {tiempo}s).")
        finally:
            Cliente.semaforo.release()


if __name__ == "__main__":
    print("=== Carnicería abierta ===\n")

    hilos = [Cliente(f"C{i+1}") for i in range(10)]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\n=== Carnicería cerrada ===")