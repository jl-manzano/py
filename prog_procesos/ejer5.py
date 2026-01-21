from multiprocessing import Process

def sumar_rango(valor1, valor2):
    if valor1 < valor2:
        inicio = valor1
        fin = valor2
    else:
        inicio = valor2
        fin = valor1

    suma = sum(range(inicio, fin+1))

    print(f"Suma de {inicio} hasta {fin}: {suma}")

if __name__ == '__main__':
    p1 = Process(target=sumar_rango, args=(1, 10))
    p2 = Process(target=sumar_rango, args=(20, 5))
    p3 = Process(target=sumar_rango, args=(50, 100))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Todos los procesos han terminado")