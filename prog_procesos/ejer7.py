from multiprocessing import Process, Queue

def leer_fichero(cola):
    with open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\prog_procesos\\pares_numeros.txt', 'r') as fichero:
        for linea in fichero:
            numeros = linea.split()
            valor1 = int(numeros[0])
            valor2 = int(numeros[1])

            cola.put((valor1, valor2))

        cola.put(None)

def sumar_rangos(cola):
    par = cola.get()

    while par is not None:
        valor1, valor2 = par

        if valor1 < valor2:
            inicio = valor1
            fin = valor2
        else:
            inicio = valor2
            fin = valor1
        
        suma = sum(range(inicio, fin + 1))
        print(f"Suma de {inicio} hasta {fin}: {suma}")

        par = cola.get()

if __name__ == '__main__':
    queue = Queue()
    
    p1 = Process(target=leer_fichero, args=(queue,))
    p2 = Process(target=sumar_rangos, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Todos los procesos han terminado")