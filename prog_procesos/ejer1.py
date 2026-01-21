from multiprocessing import Process

def sumar_numeros(limite):
    suma = sum(range(1, limite + 1))
    print(f"Suma de 1 hasta {limite}: {suma}")

if __name__ == '__main__':
    # Crear procesos
    p1 = Process(target=sumar_numeros, args=(10,))
    p2 = Process(target=sumar_numeros, args=(20,))
    p3 = Process(target=sumar_numeros, args=(50,))
    
    # Iniciar procesos
    p1.start()
    p2.start()
    p3.start()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    p3.join()
    
    print("Todos los procesos han terminado")