"""
Carrera con Barrier + Event para la cuenta atrás.

- Barrier(10): espera a que los 10 participantes estén en la línea de salida.
- Event: el hilo principal hace la cuenta atrás y luego dispara la salida con set().
- Los participantes esperan el evento (pistoletazo) con wait().
"""

import threading
import random
import time

# Barrera: espera a que todos los participantes estén listos
barrera = threading.Barrier(10)

# Evento: señal de salida (pistoletazo)
pistoletazo = threading.Event()


class Participante(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        # Simulamos que cada participante tarda un poco en llegar a la línea
        time.sleep(random.uniform(0, 2))
        print(f"{self.name} está en la línea de salida.")

        # Espera a que todos estén listos
        barrera.wait()

        # Espera el pistoletazo
        pistoletazo.wait()

        # ¡Corre!
        inicio = time.time()
        tiempo_carrera = random.uniform(5, 15)
        print(f"{self.name} ha salido.")
        time.sleep(tiempo_carrera)
        fin = time.time()

        print(f"🏁 {self.name} ha terminado la carrera en {fin - inicio:.2f} segundos.")


if __name__ == "__main__":
    nombres = [f"Corredor-{i+1}" for i in range(10)]
    hilos = [Participante(n) for n in nombres]

    for h in hilos:
        h.start()

    # El hilo principal espera a que la barrera se libere (todos están listos)
    # y luego hace la cuenta atrás
    barrera.wait()

    print("\n¡Todos los participantes están en la línea de salida!")
    for cuenta in range(3, 0, -1):
        print(f"  {cuenta}...")
        time.sleep(1)

    print("  ¡YA! 🔫\n")
    pistoletazo.set()

    for h in hilos:
        h.join()

    print("\n=== Carrera finalizada ===")