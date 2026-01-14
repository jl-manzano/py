"""
EJERCICIO 8: Lectura de pares de números con Pipe
Lee dos números por línea del fichero y calcula la suma usando tuberías
"""

from multiprocessing import Process, Pipe
import time
import os

def leer_pares_pipe(nombre_fichero, conn):
    """Lee pares de números de un fichero y los envía por pipe"""
    print(f"[Lector] Leyendo pares del fichero {nombre_fichero}")
    try:
        with open(nombre_fichero, 'r') as f:
            for linea in f:
                numeros = linea.strip().split()
                if len(numeros) == 2:
                    a, b = int(numeros[0]), int(numeros[1])
                    conn.send((a, b))
                    print(f"[Lector] Enviado: ({a}, {b})")
        # Señal de fin
        conn.send(None)
        print("[Lector] Fin de lectura, enviado None")
    except FileNotFoundError:
        print(f"[Lector] Error: No se encuentra el fichero {nombre_fichero}")
        conn.send(None)
    finally:
        conn.close()

def sumar_pares_pipe(conn):
    """Recibe pares de números por pipe y calcula la suma entre ellos"""
    print("[Sumador] Esperando pares del pipe...")
    
    while True:
        datos = conn.recv()
        
        if datos is None:
            print("[Sumador] Recibido None, terminando")
            break
        
        a, b = datos
        inicio = min(a, b)
        fin = max(a, b)
        resultado = sum(range(inicio, fin + 1))
        print(f"[Sumador] Suma de {a} a {b}: {resultado}")
    
    conn.close()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 8: Pares de números con Pipe")
    print("="*60)
    
    # Crear fichero de ejemplo
    nombre_fichero = "pares_pipe.txt"
    with open(nombre_fichero, 'w') as f:
        pares = [(1, 10), (5, 15), (20, 10), (1, 100)]
        for a, b in pares:
            f.write(f"{a} {b}\n")
    print(f"📄 Creado fichero '{nombre_fichero}' con pares de números\n")
    
    inicio = time.time()
    
    # Crear pipe
    left, right = Pipe()
    
    # Crear procesos
    p1 = Process(target=leer_pares_pipe, args=(nombre_fichero, left))
    p2 = Process(target=sumar_pares_pipe, args=(right,))
    
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