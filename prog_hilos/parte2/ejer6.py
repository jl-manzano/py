"""
Problema de los 5 filósofos de Dijkstra.

Solución para evitar interbloqueo:
    El filósofo 4 (el último) coge los palillos en orden INVERSO (derecho primero, luego izquierdo).
    Así se rompe la espera circular que provoca el deadlock.

Respuestas a las preguntas del enunciado:
    ¿Se llega a producir un interbloqueo?
        Con la solución implementada (filósofo 4 coge palillos en orden inverso), NO se produce
        interbloqueo. Sin esta corrección, podría ocurrir que cada filósofo cogiera su palillo
        izquierdo y todos quedaran esperando el derecho indefinidamente.

    ¿Podría algún filósofo no comer nunca (inanición)?
        Teóricamente sí. Si los filósofos adyacentes al filósofo i se turnan perfectamente para
        comer, podría ocurrir que uno de los palillos de i nunca quedara libre al mismo tiempo
        que el otro. En la práctica, con tiempos aleatorios, es extremadamente improbable, pero
        no imposible en términos teóricos. Esta solución no garantiza equidad (fairness).
"""

import threading
import random
import time

NUM_FILOSOFOS = 5

# Un Lock por palillo
palillos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]


class Filosofo(threading.Thread):
    def __init__(self, indice):
        threading.Thread.__init__(self, name=f"Filósofo-{indice}")
        self.indice = indice
        self.izquierdo = indice
        self.derecho = (indice + 1) % NUM_FILOSOFOS

    def run(self):
        for _ in range(3):  # Cada filósofo come 3 veces
            self._pensar()
            self._comer()

    def _pensar(self):
        tiempo = random.uniform(1, 3)
        print(f"{self.name} está pensando ({tiempo:.1f}s)...")
        time.sleep(tiempo)

    def _comer(self):
        # El filósofo 4 coge los palillos en orden inverso para evitar deadlock
        if self.indice == NUM_FILOSOFOS - 1:
            primer_palillo  = self.derecho
            segundo_palillo = self.izquierdo
        else:
            primer_palillo  = self.izquierdo
            segundo_palillo = self.derecho

        palillos[primer_palillo].acquire()
        print(f"{self.name} coge el palillo {primer_palillo}.")
        palillos[segundo_palillo].acquire()
        print(f"{self.name} coge el palillo {segundo_palillo} y COME.")

        tiempo = random.uniform(1, 2)
        time.sleep(tiempo)

        palillos[segundo_palillo].release()
        palillos[primer_palillo].release()
        print(f"{self.name} deja los palillos {primer_palillo} y {segundo_palillo} y vuelve a pensar.")


if __name__ == "__main__":
    print("=== Mesa de filósofos ===\n")

    filosofos = [Filosofo(i) for i in range(NUM_FILOSOFOS)]

    for f in filosofos:
        f.start()
    for f in filosofos:
        f.join()

    print("\n=== Todos los filósofos han comido 3 veces ===")