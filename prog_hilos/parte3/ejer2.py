"""
Escape Room con Lock + Barrier.

- Lock: protege la comprobación y escritura de 'codigo_adivinado' (igual que el número oculto).
- Barrier(5): una vez alguien adivina el código, todos esperan en la barrera
  para salir juntos.
"""

import threading
import random
import time

CODIGO_SECRETO = random.randint(1000, 9999)


class Persona(threading.Thread):
    codigo_adivinado = False
    lock = threading.Lock()
    # Barrera: las 5 personas esperan para salir juntas
    barrera = threading.Barrier(5)

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        intentos = 0
        print(f"{self.name} empieza a buscar el código...")

        while True:
            intento = random.randint(1000, 9999)
            intentos += 1
            time.sleep(random.uniform(0.01, 0.05))  # Simula tiempo de pensar

            with Persona.lock:
                if intento == CODIGO_SECRETO and not Persona.codigo_adivinado:
                    Persona.codigo_adivinado = True
                    print(f"\n🔓 ¡{self.name} ha adivinado el código {intento} en {intentos} intentos!")
                    print(f"   Avisando al resto para salir juntos...\n")
                    break
                elif Persona.codigo_adivinado:
                    print(f"{self.name} se entera de que alguien ha adivinado el código (llevaba {intentos} intentos).")
                    break

        # Todas las personas esperan aquí antes de salir
        print(f"{self.name} está esperando en la puerta para salir con el grupo.")
        Persona.barrera.wait()
        print(f"🚪 {self.name} sale de la Escape Room.")


if __name__ == "__main__":
    print(f"[DEBUG] Código secreto: {CODIGO_SECRETO}\n")
    print("=== Escape Room iniciada ===\n")

    personas = [Persona(f"Persona-{i+1}") for i in range(5)]

    for p in personas:
        p.start()
    for p in personas:
        p.join()

    print("\n=== ¡Todos han escapado! ===")