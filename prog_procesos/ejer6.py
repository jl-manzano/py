from multiprocessing import Pool

def sumar_rango(valor1, valor2):
    if valor1 < valor2:
        inicio = valor1
        fin = valor2
    else:
        inicio = valor2
        fin = valor1

    suma = sum(range(inicio, fin + 1))

    resultado = f"Suma de {inicio} hasta {fin}: {suma}"
    return resultado

if __name__ == '__main__':
    numeros = [(1, 10), (20, 5), (50, 100), (30, 40)]

    with Pool() as pool:
        resultados = pool.starmap(sumar_rango, numeros)

    print("\nTodos los procesos han terminado")
