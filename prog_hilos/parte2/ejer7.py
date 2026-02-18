"""
Problema Productor-Consumidor con cola de máximo 1 elemento.

Se usan dos Conditions (o un Condition con lógica de espera) para sincronizar:
    - El PRODUCTOR espera si la cola está llena.
    - El CONSUMIDOR espera si la cola está vacía.

¿Cambiaría mucho la solución si el máximo son 5 elementos?
    La lógica es prácticamente idéntica: solo cambia el valor MAX_COLA de 1 a 5.
    Con MAX_COLA=1 el productor y consumidor se alternan casi obligatoriamente.
    Con MAX_COLA=5 el productor puede adelantarse hasta 5 elementos antes de bloquearse,
    lo que da más margen y reduce el número de esperas, pero el código es el mismo.
    En ambos casos las condiciones de espera son:
        - Productor espera si len(cola) == MAX_COLA
        - Consumidor espera si len(cola) == 0
"""

import threading
import random
import time

MAX_COLA = 1   # Cambia a 5 para probar la variante de 5 elementos

class ColaCompartida:
    def __init__(self, maxima):
        self.cola = []
        self.maxima = maxima
        self.cond = threading.Condition()

    def producir(self, dato, nombre):
        with self.cond:
            while len(self.cola) >= self.maxima:
                print(f"  [PRODUCTOR {nombre}] Cola llena ({self.cola}), esperando...")
                self.cond.wait()
            self.cola.append(dato)
            print(f"  [PRODUCTOR {nombre}] Produce '{dato}' -> cola: {self.cola}")
            self.cond.notify_all()

    def consumir(self, nombre):
        with self.cond:
            while len(self.cola) == 0:
                print(f"  [CONSUMIDOR {nombre}] Cola vacía, esperando...")
                self.cond.wait()
            dato = self.cola.pop(0)
            print(f"  [CONSUMIDOR {nombre}] Consume '{dato}' -> cola: {self.cola}")
            self.cond.notify_all()
            return dato


# Cola compartida global
cola = ColaCompartida(MAX_COLA)


class Productor(threading.Thread):
    def __init__(self, nombre, num_items):
        threading.Thread.__init__(self, name=nombre)
        self.num_items = num_items

    def run(self):
        for i in range(self.num_items):
            dato = f"item-{self.name}-{i}"
            time.sleep(random.uniform(0.5, 1.5))  # Tiempo de producción
            cola.producir(dato, self.name)


class Consumidor(threading.Thread):
    def __init__(self, nombre, num_items):
        threading.Thread.__init__(self, name=nombre)
        self.num_items = num_items

    def run(self):
        for _ in range(self.num_items):
            time.sleep(random.uniform(0.5, 2.0))  # Tiempo de consumo
            dato = cola.consumir(self.name)
            print(f"  [CONSUMIDOR {self.name}] Procesando '{dato}'...")


if __name__ == "__main__":
    print(f"=== Productor-Consumidor (cola máx. {MAX_COLA}) ===\n")

    # 2 productores que producen 5 items cada uno = 10 items en total
    # 2 consumidores que consumen 5 items cada uno
    productores  = [Productor(f"P{i+1}", 5) for i in range(2)]
    consumidores = [Consumidor(f"C{i+1}", 5) for i in range(2)]

    hilos = productores + consumidores
    for h in hilos:
        h.start()
    for h in hilos:
        h.join()

    print("\n=== Fin de la simulación ===")
    print(f"Cola final (debe estar vacía): {cola.cola}")