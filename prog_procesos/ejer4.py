from multiprocessing import Process, Pipe
import time
import os

def leer_numeros_pipe(nombre_fichero, conn):
    """Lee números de un fichero y los envía por pipe"""
    print(f"[Lector] Leyendo números del fichero {nombre_fichero}")
    try:
        with open(nombre_fichero, 'r') as f:
            for linea in f:
                numero = int(linea.strip())
                conn.send(numero)
                print(f"[Lector] Enviado: {numero}")
        # Señal de fin
        conn.send(None)
        print("[Lector] Fin de lectura, enviado None")
    except FileNotFoundError:
        print(f"[Lector] Error: No se encuentra el fichero {nombre_fichero}")
        conn.send(None)
    finally:
        conn.close()

def sumar_desde_pipe(conn):
    """Recibe números por pipe y los suma"""
    suma_total = 0
    contador = 0
    
    print("[Sumador] Esperando números del pipe...")
    
    while True:
        numero = conn.recv()
        
        if numero is None:
            print("[Sumador] Recibido None, terminando suma")
            break
        
        suma_total += numero
        contador += 1
        print(f"[Sumador] Recibido: {numero}, Suma parcial: {suma_total}")
    
    print(f"\n[Sumador] RESULTADO FINAL: {suma_total} (sumados {contador} números)")
    conn.close()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("EJERCICIO 4: Comunicación con Pipe")
    print("="*60)
    
    # Crear fichero de ejemplo
    nombre_fichero = "numeros_pipe.txt"
    with open(nombre_fichero, 'w') as f:
        for i in range(1, 11):
            f.write(f"{i}\n")
    print(f"📄 Creado fichero '{nombre_fichero}' con números del 1 al 10\n")
    
    inicio = time.time()
    
    # Crear pipe
    left, right = Pipe()
    
    # Crear procesos
    p1 = Process(target=leer_numeros_pipe, args=(nombre_fichero, left))
    p2 = Process(target=sumar_desde_pipe, args=(right,))
    
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
