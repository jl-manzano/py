from multiprocessing import Pool
import time

def sumar_numeros(limite):
    suma = sum(range(1, limite + 1))
    return suma

if __name__ == '__main__':

    numeros = [5, 10, 20, 22]

    with Pool(processes=len(numeros)) as pool:

        inicio = time.perf_counter()
        
        results = pool.map(sumar_numeros, numeros)

        final = time.perf_counter()

        print("Resultados:", results)
        print(f"Tiempo: {final - inicio}")
        
