"""
Paso de peatones con Barrier + Timer.

- Los peatones esperan en una Barrier hasta que el semáforo se pone en verde.
- Un Timer periódico simula el cambio de luz: cada vez que se libera la barrera,
  se programa otro Timer para la siguiente vez (semáforo en rojo → verde).
- Se usa un Event para indicar cuándo el semáforo está en verde.
"""

import threading
import random
import time

# Evento: semáforo en verde (set) o rojo (not set)
semaforo_verde = threading.Event()

# Número de peatones en la simulación
NUM_PEATONES = 8

# Tiempo entre cambios de semáforo (en segundos)
TIEMPO_ROJO  = 6
TIEMPO_VERDE = 3


def cambiar_a_verde():
    """Pone el semáforo en verde y lo apaga tras TIEMPO_VERDE segundos."""
    print("\n🟢 Semáforo en VERDE — ¡Los peatones pueden cruzar!\n")
    semaforo_verde.set()
    # Tras TIEMPO_VERDE segundos vuelve a rojo
    apagador = threading.Timer(TIEMPO_VERDE, cambiar_a_rojo)
    apagador.daemon = True
    apagador.start()


def cambiar_a_rojo():
    """Pone el semáforo en rojo y programa el siguiente verde."""
    print("\n🔴 Semáforo en ROJO — Los peatones deben esperar.\n")
    semaforo_verde.clear()
    # Programa el siguiente cambio a verde
    encendedor = threading.Timer(TIEMPO_ROJO, cambiar_a_verde)
    encendedor.daemon = True
    encendedor.start()


class Peaton(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        # El peatón llega en un momento aleatorio
        time.sleep(random.uniform(0, 4))
        print(f"🧍 {self.name} llega al paso de peatones y espera.")

        # Espera a que el semáforo esté en verde
        semaforo_verde.wait()

        # Cruza la calle
        tiempo_cruce = random.uniform(1, 3)
        print(f"🚶 {self.name} está cruzando la calle ({tiempo_cruce:.1f}s)...")
        time.sleep(tiempo_cruce)
        print(f"✅ {self.name} ha cruzado.")


if __name__ == "__main__":
    print("=== Simulador de paso de peatones ===\n")
    print(f"🔴 Semáforo arranca en ROJO. Primer verde en {TIEMPO_ROJO}s.\n")

    # Arranca el ciclo del semáforo
    primer_cambio = threading.Timer(TIEMPO_ROJO, cambiar_a_verde)
    primer_cambio.daemon = True
    primer_cambio.start()

    # Lanza los peatones
    peatones = [Peaton(f"Peatón-{i+1}") for i in range(NUM_PEATONES)]
    for p in peatones:
        p.start()
    for p in peatones:
        p.join()

    print("\n=== Todos los peatones han cruzado ===")