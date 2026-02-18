import threading
import random
import time

# 9 libros: True = libre, False = ocupado
class Biblioteca:
    libros = [True] * 9
    cond = threading.Condition()

    @classmethod
    def coger_libros(cls, nombres_libros):
        """Espera hasta que los dos libros indicados estén libres y los reserva."""
        with cls.cond:
            while not (cls.libros[nombres_libros[0]] and cls.libros[nombres_libros[1]]):
                cls.cond.wait()
            # Ambos libros están libres: los reservamos
            cls.libros[nombres_libros[0]] = False
            cls.libros[nombres_libros[1]] = False

    @classmethod
    def devolver_libros(cls, nombres_libros):
        """Devuelve los dos libros y notifica a los hilos en espera."""
        with cls.cond:
            cls.libros[nombres_libros[0]] = True
            cls.libros[nombres_libros[1]] = True
            cls.cond.notify_all()


class Estudiante(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        # Selecciona 2 libros distintos al azar
        indices = random.sample(range(9), 2)
        libro_a = indices[0] + 1  # Numeramos los libros del 1 al 9
        libro_b = indices[1] + 1

        print(f"Estudiante {self.name} quiere los libros {libro_a} y {libro_b}.")

        Biblioteca.coger_libros([indices[0], indices[1]])

        print(f"Estudiante {self.name} ha cogido los libros {libro_a} y {libro_b} y los está usando.")
        tiempo = random.randint(3, 5)
        time.sleep(tiempo)

        Biblioteca.devolver_libros([indices[0], indices[1]])

        print(f"Estudiante {self.name} ha devuelto los libros {libro_a} y {libro_b}.")


if __name__ == "__main__":
    print("=== Biblioteca abierta ===\n")

    # 4 estudiantes, cada uno usa los libros varias veces
    estudiantes = ["Alicia", "Bruno", "Carmen", "David"]
    hilos = []

    for nombre in estudiantes:
        hilo = Estudiante(nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\n=== Todos los estudiantes han terminado ===")