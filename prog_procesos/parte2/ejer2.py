from multiprocessing import Process, Pipe
import random
import time

def generar_ips(conn):
    """Proceso 1: Genera 10 direcciones IP aleatorias"""
    print("\n[Proceso 1] Generando 10 direcciones IP...")
    
    for i in range(10):
        # Generar IP aleatoria
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        print(f"[Proceso 1] IP generada: {ip}")
        conn.send(ip)
        time.sleep(0.1)  # Pequeña pausa para simular procesamiento
    
    conn.send(None)
    conn.close()
    print("[Proceso 1] Finalizado\n")

def filtrar_ips(conn_entrada, conn_salida):
    """Proceso 2: Filtra IPs de clases A, B o C"""
    print("[Proceso 2] Esperando direcciones IP...\n")
    
    ip = conn_entrada.recv()
    contador = 0
    
    while ip is not None:
        # Obtener primer octeto
        primer_octeto = int(ip.split('.')[0])
        
        # Verificar si es clase A (1-126), B (128-191) o C (192-223)
        if (1 <= primer_octeto <= 126) or (128 <= primer_octeto <= 191) or (192 <= primer_octeto <= 223):
            print(f"[Proceso 2] IP válida (clase A/B/C): {ip}")
            conn_salida.send(ip)
            contador += 1
        else:
            print(f"[Proceso 2] IP descartada (no es A/B/C): {ip}")
        
        ip = conn_entrada.recv()
    
    conn_salida.send(None)
    conn_entrada.close()
    conn_salida.close()
    print(f"\n[Proceso 2] Finalizado - {contador} IPs enviadas al Proceso 3\n")

def clasificar_ips(conn):
    """Proceso 3: Clasifica y muestra las IPs recibidas"""
    print("[Proceso 3] Esperando direcciones IP filtradas...\n")
    
    ip = conn.recv()
    
    while ip is not None:
        primer_octeto = int(ip.split('.')[0])
        
        # Determinar la clase
        if 1 <= primer_octeto <= 126:
            clase = "A"
        elif 128 <= primer_octeto <= 191:
            clase = "B"
        elif 192 <= primer_octeto <= 223:
            clase = "C"
        else:
            clase = "Desconocida"
        
        print(f"[Proceso 3] {ip} - Clase {clase}")
        
        ip = conn.recv()
    
    conn.close()
    print("\n[Proceso 3] Finalizado")

if __name__ == '__main__':
    print("=== SISTEMA DE PROCESAMIENTO DE IPs ===")
    
    inicio = time.perf_counter()
    
    # Crear dos pipes para conectar los tres procesos
    pipe1_left, pipe1_right = Pipe()  # Proceso 1 -> Proceso 2
    pipe2_left, pipe2_right = Pipe()  # Proceso 2 -> Proceso 3
    
    # Crear los tres procesos
    p1 = Process(target=generar_ips, args=(pipe1_right,))
    p2 = Process(target=filtrar_ips, args=(pipe1_left, pipe2_right))
    p3 = Process(target=clasificar_ips, args=(pipe2_left,))
    
    # Lanzar procesos en orden
    p1.start()
    p2.start()
    p3.start()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    p3.join()
    
    final = time.perf_counter()
    
    print("\n" + "="*50)
    print(f"Tiempo de ejecución: {final - inicio:.4f} segundos")
    print("Todos los procesos han terminado")