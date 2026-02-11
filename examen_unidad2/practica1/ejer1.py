from multiprocessing import Process, Pool
import random
import os

# obtiene la carpeta donde está el script
carpeta = os.path.dirname(os.path.abspath(__file__))

def generar_temperaturas(dia):
    """Proceso 1: Genera 24 temperaturas aleatorias para un día"""
    temperaturas = [round(random.uniform(0.0, 20.0), 2) for _ in range(24)]
    nombre_fichero = os.path.join(carpeta, f"{dia:02d}-12.txt")
    
    with open(nombre_fichero, 'w') as fichero:
        for temp in temperaturas:
            fichero.write(f"{temp}\n")
    
    return nombre_fichero

def obtener_maxima(nombre_fichero):
    """Proceso 2: Lee temperaturas y escribe la máxima en maximas.txt"""
    fecha = os.path.basename(nombre_fichero).replace('.txt', '')
    
    with open(nombre_fichero, 'r') as fichero:
        temperaturas = [float(linea.strip()) for linea in fichero]
    
    temp_maxima = max(temperaturas)
    
    with open(os.path.join(carpeta, 'maximas.txt'), 'a') as fichero:
        fichero.write(f"{fecha}:{temp_maxima}\n")

def obtener_minima(nombre_fichero):
    """Proceso 3: Lee temperaturas y escribe la mínima en minimas.txt"""
    fecha = os.path.basename(nombre_fichero).replace('.txt', '')
    
    with open(nombre_fichero, 'r') as fichero:
        temperaturas = [float(linea.strip()) for linea in fichero]
    
    temp_minima = min(temperaturas)
    
    with open(os.path.join(carpeta, 'minimas.txt'), 'a') as fichero:
        fichero.write(f"{fecha}:{temp_minima}\n")

if __name__ == '__main__':
    # Limpiar archivos anteriores
    if os.path.exists(os.path.join(carpeta, 'maximas.txt')):
        os.remove(os.path.join(carpeta, 'maximas.txt'))
    if os.path.exists(os.path.join(carpeta, 'minimas.txt')):
        os.remove(os.path.join(carpeta, 'minimas.txt'))
    
    NUM_DIAS = 31
    dias = list(range(1, NUM_DIAS + 1))
    ficheros = [os.path.join(carpeta, f"{dia:02d}-12.txt") for dia in dias]
    
    # generar temperaturas de 31 días simultáneamente con Pool
    with Pool(processes=NUM_DIAS) as pool:
        pool.map(generar_temperaturas, dias)
    
    print(f"[PASO 1] {NUM_DIAS} ficheros de temperaturas generados")
    
    # lanzar proceso 2 y proceso 3 simultáneamente (31 veces cada uno)
    procesos_maximas = []
    procesos_minimas = []
    
    for fichero in ficheros:
        p2 = Process(target=obtener_maxima, args=(fichero,))
        p3 = Process(target=obtener_minima, args=(fichero,))
        procesos_maximas.append(p2)
        procesos_minimas.append(p3)
        p2.start()
        p3.start()
    
    for p in procesos_maximas:
        p.join()
    for p in procesos_minimas:
        p.join()
    
    print("[PASO 2] maximas.txt y minimas.txt generados")
    print("Todos los procesos han terminado")