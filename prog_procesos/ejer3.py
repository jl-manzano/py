from multiprocessing import Process, Queue
import time
import os

def leer_numeros_queue(nombre_fichero, cola):
    """Lee números de un fichero y los añade a una cola"""
    print(f"[Lector] Leyendo números del fichero {nombre_fichero}")
    try:
        with open(nombre_fichero, 'r') as f:
            for linea in f:
                numero = int(linea.strip())
                cola.put(numero)
                print(f"[Lector] Añadido a la cola: {numero}")
        # Señal de fin
        cola.put(None)
        print("[Lector] Fin de lectura, enviado None")
    except FileNotFoundError:
        print(f"[Lector] Error: No se encuentra el fichero {nombre_fichero}")
        cola.put(None)

def sumar_desde_queue(cola):
    """Lee números de una cola y los suma"""
    suma_total = 0
    contador = 0
    
    print("[Sumador] Esperando números de la cola...")
    
    while True:
        numero = cola.get()
        
        if numero is None:
            print("[Sumador] Recibido None, terminando suma")
            break
        
        suma_total += numero
        contador += 1
        print(f"[Sumador] Recibido: {numero}, Suma parcial: {suma_total}")
    
    print(f"\n[Sumador] RESULTADO FINAL: {suma_total} (sumados {contador} números)")

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 3: Comunicación con Queue")
    print("="*60)
    
    # Crear fichero de ejemplo
    nombre_fichero = "numeros.txt"
    with open(nombre_fichero, 'w') as f:
        for i in range(1, 11):
            f.write(f"{i}\n")
    print(f"📄 Creado fichero '{nombre_fichero}' con números del 1 al 10\n")
    
    inicio = time.time()
    
    # Crear cola compartida
    cola = Queue()
    
    # Crear procesos
    p1 = Process(target=leer_numeros_queue, args=(nombre_fichero, cola))
    p2 = Process(target=sumar_desde_queue, args=(cola,))
    
    # Iniciar procesos
    p1.start()
    p2.start()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    
    print("\n✓ Todos los procesos han terminado")
    
    fin = time.time()
    print(f"⏱️  Tiempo de ejecución: {fin - inicio:.4f} segundos")
    
    # Limpiar
    os.remove(nombre_fichero)
