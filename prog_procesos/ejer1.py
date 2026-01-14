"""
EJERCICIO 1: Suma desde 1 hasta N con Process
Crea varios procesos que sumen números desde 1 hasta un valor dado
"""

from multiprocessing import Process
import time
import os

def suma_hasta_n(n):
    """Suma todos los números desde 1 hasta n"""
    resultado = sum(range(1, n + 1))
    print(f"[Proceso {os.getpid()}] Suma desde 1 hasta {n}: {resultado}")
    return resultado

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 1: Suma con Process")
    print("="*60)
    
    inicio = time.time()
    
    # Crear varios procesos
    procesos = []
    valores = [1000, 2000, 3000, 4000]
    
    for valor in valores:
        p = Process(target=suma_hasta_n, args=(valor,))
        procesos.append(p)
        p.start()
    
    # Esperar a que todos terminen
    for p in procesos:
        p.join()
    
    print("\n✓ Todos los procesos han terminado")
    
    fin = time.time()
    print(f"⏱️  Tiempo de ejecución: {fin - inicio:.4f} segundos")