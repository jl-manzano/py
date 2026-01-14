from multiprocessing import Process, Queue
import time
import os

def leer_pares_queue(nombre_fichero, cola):
    """Lee pares de números de un fichero y los añade a una cola"""
    print(f"[Lector] Leyendo pares del fichero {nombre_fichero}")
    try:
        with open(nombre_fichero, 'r') as f:
            for linea in f:
                numeros = linea.strip().split()
                if len(numeros) == 2:
                    a, b = int(numeros[0]), int(numeros[1])
                    cola.put((a, b))
                    print(f"[Lector] Añadido a la cola: ({a}, {b})")
        # Señal de fin
        cola.put(None)
        print("[Lector] Fin de lectura, enviado None")
    except FileNotFoundError:
        print(f"[Lector] Error: No se encuentra el fichero {nombre_fichero}")
        cola.put(None)

def sumar_pares_queue(cola):
    """Lee pares de números de una cola y calcula la suma entre ellos"""
    suma_total = 0
    contador = 0
    print("[Sumador] Esperando pares de la cola...")
    
    # Recoger todos los elementos hasta recibir None
    datos = cola.get()
    while datos is not None:
        a, b = datos
        inicio = min(a, b)
        fin = max(a, b)
        resultado = sum(range(inicio, fin + 1))
        print(f"[Sumador] Suma de {a} a {b}: {resultado}")
        
        contador += 1
        datos = cola.get()  # Obtener siguiente par
    
    print(f"\n[Sumador] RESULTADO FINAL: Suma total de {contador} pares procesados")

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 7: Pares de números con Queue")
    print("="*60)
    
    # Crear fichero de ejemplo
    nombre_fichero = "pares.txt"
    with open(nombre_fichero, 'w') as f:
        pares = [(1, 10), (5, 15), (20, 10), (1, 100)]
        for a, b in pares:
            f.write(f"{a} {b}\n")
    print(f"📄 Creado fichero '{nombre_fichero}' con pares de números\n")
    
    inicio = time.time()
    
    # Crear cola compartida
    cola = Queue()
    
    # Crear procesos
    p1 = Process(target=leer_pares_queue, args=(nombre_fichero, cola))
    p2 = Process(target=sumar_pares_queue, args=(cola,))
    
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
