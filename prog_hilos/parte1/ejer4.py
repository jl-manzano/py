import threading

# Texto de ejemplo sobre el que contar vocales
TEXTO = """
La programación concurrente permite que varios procesos o hilos se ejecuten 
de manera simultánea o aparentemente simultánea. Esto puede mejorar el rendimiento 
de las aplicaciones, especialmente en sistemas con múltiples núcleos de procesamiento. 
Sin embargo, la concurrencia también introduce desafíos como las condiciones de carrera 
y los problemas de sincronización que deben ser cuidadosamente gestionados.
"""

class ContadorVocal(threading.Thread):
    # Variable compartida: diccionario con el conteo de cada vocal
    resultados = {}

    def __init__(self, vocal):
        threading.Thread.__init__(self, name=f"Hilo-{vocal.upper()}")
        self.vocal = vocal

    def run(self):
        texto_lower = TEXTO.lower()
        cuenta = texto_lower.count(self.vocal)
        ContadorVocal.resultados[self.vocal] = cuenta
        print(f"{self.name}: encontradas {cuenta} '{self.vocal}'")


if __name__ == "__main__":
    vocales = ['a', 'e', 'i', 'o', 'u']

    print("Texto analizado:")
    print(TEXTO)
    print("Contando vocales con hilos...\n")

    hilos = []
    for vocal in vocales:
        hilo = ContadorVocal(vocal)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    total = sum(ContadorVocal.resultados.values())
    print("\n--- Resultados finales ---")
    for vocal, cuenta in sorted(ContadorVocal.resultados.items()):
        print(f"  '{vocal}': {cuenta}")
    print(f"  Total vocales: {total}")