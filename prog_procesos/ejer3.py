from multiprocessing import Process, Queue

def leer_fichero(cola):
    with open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\prog_procesos\\numeros.txt', 'r') as fichero:
        for linea in fichero:
            numero = int(linea)
            cola.put(numero)

    cola.put(None)

def sumar_numeros(cola):
    suma = 0
    numero = cola.get()

    while numero is not None:
        suma += numero
        numero = cola.get()

    print(f"Suma total: {suma}")

if __name__ == '__main__':
    cola = Queue()

    p1 = Process(target=leer_fichero, args=(cola,))
    p2 = Process(target=sumar_numeros, args=(cola,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Todos los procesos han terminado")
