import threading

class Contador(threading.Thread):
    # Variable compartida por todos los objetos de la clase
    contador = 0

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while Contador.contador < 1000:
            Contador.contador += 1
            print(f"Hilo {self.name} -> contador = {Contador.contador}")


if __name__ == "__main__":
    hilos = []
    for i in range(10):
        hilo = Contador(str(i))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"\n--- Valor final del contador: {Contador.contador} ---")
    print("Nota: El valor puede superar 1000 debido a condiciones de carrera (race conditions).")
    print("Varios hilos pueden leer el contador < 1000 al mismo tiempo y luego incrementarlo.")