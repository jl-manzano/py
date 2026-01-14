"""
EJERCICIO 6: Suma entre dos valores con Pool y starmap
Usa starmap para pasar múltiples argumentos a cada proceso
"""

from multiprocessing import Pool
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
    print("EJERCICIO 6: Suma entre dos valores con Pool (starmap)")
    print("="*60)
    
    rangos = [(1, 100), (50, 150), (200, 100), (1, 500), (300, 600)]
    
    # Probar con diferentes números de procesos
    for num_procesos in [2, 3, 4]:
        print(f"\n--- Con {num_procesos} procesos ---")
        inicio = time.time()
        
        with Pool(processes=num_procesos) as pool:
            # starmap para funciones con múltiples argumentos
            resultados = pool.starmap(suma_entre_valores, rangos)
        
        print(f"Resultados: {resultados}")
        
        fin = time.time()
        print(f"⏱️  Tiempo con {num_procesos} procesos: {fin - inicio:.4f} segundos")