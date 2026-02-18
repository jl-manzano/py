import threading
import random
import time

class Cliente(threading.Thread):
    # 4 empleados en carnicería, 2 en charcutería
    sem_carniceria  = threading.Semaphore(4)
    sem_charcuteria = threading.Semaphore(2)

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def _ir_a_carniceria(self):
        print(f"  [{self.name}] Esperando para entrar a Carnicería...")
        Cliente.sem_carniceria.acquire()
        try:
            print(f"  [{self.name}] >>> Siendo atendido en CARNICERÍA.")
            tiempo = random.randint(1, 8)
            time.sleep(tiempo)
            print(f"  [{self.name}] <<< Terminó en CARNICERÍA (tardó {tiempo}s).")
        finally:
            Cliente.sem_carniceria.release()

    def _ir_a_charcuteria(self):
        print(f"  [{self.name}] Esperando para entrar a Charcutería...")
        Cliente.sem_charcuteria.acquire()
        try:
            print(f"  [{self.name}] >>> Siendo atendido en CHARCUTERÍA.")
            tiempo = random.randint(1, 6)
            time.sleep(tiempo)
            print(f"  [{self.name}] <<< Terminó en CHARCUTERÍA (tardó {tiempo}s).")
        finally:
            Cliente.sem_charcuteria.release()

    def run(self):
        print(f"Cliente {self.name} entra a la tienda.")

        # El orden de visita es aleatorio: primero carnicería o charcutería
        if random.choice([True, False]):
            self._ir_a_carniceria()
            self._ir_a_charcuteria()
        else:
            self._ir_a_charcuteria()
            self._ir_a_carniceria()

        print(f"Cliente {self.name} ha sido completamente atendido y se va.\n")


if __name__ == "__main__":
    print("=== Tienda abierta (Carnicería + Charcutería) ===\n")

    hilos = [Cliente(f"C{i+1}") for i in range(10)]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("=== Tienda cerrada ===")