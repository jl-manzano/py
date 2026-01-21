from multiprocessing import Process, Pipe

def leer_fichero(conn):
    with open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\prog_procesos\\pares_numeros.txt', 'r') as fichero:
        for linea in fichero:
            numeros = linea.split()
            valor1 = int(numeros[0])
            valor2 = int(numeros[1])
            conn.send((valor1, valor2))
        
        conn.send(None)
        conn.close()

def sumar_numeros(conn):
    suma = 0
    par = conn.recv()

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

        par = conn.recv()

    conn.close()

if __name__ == '__main__':
    left, right = Pipe()

    p1 = Process(target=leer_fichero, args=(right,))
    p2 = Process(target=sumar_numeros, args=(left,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Todos los procesos han terminado")