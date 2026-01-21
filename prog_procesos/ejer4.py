from multiprocessing import Process, Pipe

def leer_fichero(conn):
    with open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\prog_procesos\\numeros.txt', 'r') as fichero:
        for linea in fichero:
            numero = int(linea)
            conn.send(numero)

        conn.send(None)
        conn.close()

def sumar_numeros(conn):
    suma = 0
    numero = conn.recv()

    while numero is not None:
        suma += numero
        numero = conn.recv()

    print(f"Suma total: {suma}")
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