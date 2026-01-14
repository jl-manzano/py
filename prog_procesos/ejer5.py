"""
EJERCICIO 5: Suma entre dos valores con Process
Suma todos los números comprendidos entre dos valores
"""

from multiprocessing import Process
import time
import os

def suma_entre_valores(a, b):
    """Suma todos los números entre a y b, incluyendo ambos"""
    # Asegurar que el rango esté ordenado
    inicio = min(a, b)
    fin = max(a, b)
    
    resultado = sum(range(inicio, fin + 1))
    print(f"[Proceso {os.getpid()}] Suma de {a} a {b}: {resultado}")
    return resultado

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 5: Suma entre dos valores con Process")
    print("="*60)
    
    inicio_tiempo = time.time()
    
    # Crear varios procesos con diferentes rangos
    procesos = []
    rangos = [(1, 100), (50, 150), (200, 100), (1, 500)]
    
    for a, b in rangos:
        p = Process(target=suma_entre_valores, args=(a, b))
        procesos.append(p)
        p.start()
    
    # Esperar a que todos terminen
    for p in procesos:
        p.join()
    
    print("\n✓ Todos los procesos han terminado")
    
    fin_tiempo = time.time()
    print(f"⏱️  Tiempo de ejecución: {fin_tiempo - inicio_tiempo:.4f} segundos")