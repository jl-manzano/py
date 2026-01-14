"""
EJERCICIO 2: Suma hasta N con Pool
Usa Pool para lanzar procesos de forma concurrente y compara tiempos
"""

from multiprocessing import Pool
import time
import os

def suma_hasta_n(n):
    """Suma todos los números desde 1 hasta n"""
    resultado = sum(range(1, n + 1))
    print(f"[Proceso {os.getpid()}] Suma desde 1 hasta {n}: {resultado}")
    return resultado

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 2: Suma con Pool")
    print("="*60)
    
    valores = [1000, 2000, 3000, 4000, 5000, 6000]
    
    # Probar con diferentes números de procesos
    for num_procesos in [2, 3, 4]:
        print(f"\n--- Con {num_procesos} procesos ---")
        inicio = time.time()
        
        with Pool(processes=num_procesos) as pool:
            resultados = pool.map(suma_hasta_n, valores)
        
        print(f"Resultados: {resultados}")
        
        fin = time.time()
        print(f"⏱️  Tiempo con {num_procesos} procesos: {fin - inicio:.4f} segundos")