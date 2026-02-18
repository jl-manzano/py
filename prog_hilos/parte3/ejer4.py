"""
Pedidos de almacén con Barrier + Event.

CORRECCIÓN: Se añade el evento 'trabajo_terminado' que activa el último
trabajador que completa un pedido. Los trabajadores ociosos bloqueados en
hay_pedido.wait() usan timeout=1 para poder comprobar la señal de fin.
"""

import threading
import random
import time

NUM_TRABAJADORES  = 5
NUM_PEDIDOS       = 8

barrera           = threading.Barrier(NUM_TRABAJADORES)
hay_pedido        = threading.Event()
trabajo_terminado = threading.Event()   # ← señal de fin para desbloquear ociosos

lock_pedido       = threading.Lock()

pedidos_completados = 0
lock_completados    = threading.Lock()

pedido_actual = {"id": 0, "descripcion": ""}


class Trabajador(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        global pedidos_completados

        print(f"{self.name} llega al almacén y espera a sus compañeros.")
        barrera.wait()
        print(f"{self.name} empieza su turno.")

        while not trabajo_terminado.is_set():
            # Espera pedido con timeout para poder comprobar trabajo_terminado
            hay_pedido.wait(timeout=1)

            if trabajo_terminado.is_set():
                break

            if not hay_pedido.is_set():
                continue

            # Sección crítica: solo un trabajador toma el pedido
            with lock_pedido:
                if not hay_pedido.is_set():
                    continue
                pedido_id   = pedido_actual["id"]
                descripcion = pedido_actual["descripcion"]
                hay_pedido.clear()

            tiempo = random.randint(2, 5)
            print(f"📦 {self.name} empieza a preparar el pedido #{pedido_id} ({descripcion}) — tardará {tiempo}s.")
            time.sleep(tiempo)
            print(f"✅ {self.name} ha completado el pedido #{pedido_id}.")

            with lock_completados:
                pedidos_completados += 1
                if pedidos_completados >= NUM_PEDIDOS:
                    trabajo_terminado.set()   # despierta a todos los ociosos
                    break

        print(f"{self.name} termina su turno.")


def generador_pedidos():
    productos = ["Televisores", "Neveras", "Ordenadores", "Sillas", "Mesas",
                 "Auriculares", "Teléfonos", "Tablets", "Monitores", "Teclados"]

    for i in range(1, NUM_PEDIDOS + 1):
        time.sleep(random.randint(3, 7))
        pedido_actual["id"]          = i
        pedido_actual["descripcion"] = random.choice(productos)
        print(f"\n🔔 [GENERADOR] Nuevo pedido #{i}: {pedido_actual['descripcion']}\n")
        hay_pedido.set()


if __name__ == "__main__":
    print("=== Almacén abierto ===\n")

    trabajadores = [Trabajador(f"Trabajador-{i+1}") for i in range(NUM_TRABAJADORES)]
    gen = threading.Thread(target=generador_pedidos, name="Generador", daemon=True)

    for t in trabajadores:
        t.start()
    gen.start()

    for t in trabajadores:
        t.join()

    print(f"\n=== Almacén cerrado. {pedidos_completados} pedidos completados. ===")