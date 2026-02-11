from multiprocessing import Process, Pipe
import os

# obtiene la carpeta donde está el script
carpeta = os.path.dirname(os.path.abspath(__file__))

def filtrar_departamento(departamento, conn):
    """Proceso 1: Filtra líneas por departamento y envía sin el campo departamento"""
    with open(os.path.join(carpeta, 'salarios.txt'), 'r', encoding='utf-8') as fichero:
        for linea in fichero:
            linea = linea.strip()
            if linea:
                partes = linea.split(';')
                nombre, apellido, salario, dept = partes
                
                if dept.lower() == departamento.lower():
                    conn.send(f"{nombre};{apellido};{salario}")
    
    conn.send(None)
    conn.close()

def filtrar_salario(salario_minimo, conn_entrada, conn_salida):
    """Proceso 2: Filtra por salario mínimo y reenvía las líneas que cumplen"""
    dato = conn_entrada.recv()
    
    while dato is not None:
        partes = dato.split(';')
        salario = int(partes[2])
        
        if salario >= salario_minimo:
            conn_salida.send(dato)
        
        dato = conn_entrada.recv()
    
    conn_salida.send(None)
    conn_entrada.close()
    conn_salida.close()

def escribir_fichero(conn):
    """Proceso 3: Escribe en empleados.txt con formato Apellido Nombre, Salario"""
    with open(os.path.join(carpeta, 'empleados.txt'), 'w', encoding='utf-8') as fichero:
        dato = conn.recv()
        
        while dato is not None:
            partes = dato.split(';')
            nombre, apellido, salario = partes
            fichero.write(f"{apellido} {nombre}, {salario}\n")
            dato = conn.recv()
    
    conn.close()

if __name__ == '__main__':
    # Pedir datos al usuario
    departamento = input("Introduce el nombre del departamento: ")
    salario_minimo = int(input("Introduce el salario mínimo: "))
    
    # Crear pipes para comunicación
    pipe1_izq, pipe1_der = Pipe()
    pipe2_izq, pipe2_der = Pipe()
    
    # Crear procesos
    p1 = Process(target=filtrar_departamento, args=(departamento, pipe1_der))
    p2 = Process(target=filtrar_salario, args=(salario_minimo, pipe1_izq, pipe2_der))
    p3 = Process(target=escribir_fichero, args=(pipe2_izq,))
    
    # Lanzar procesos
    p1.start()
    p2.start()
    p3.start()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    p3.join()
    
    print("Todos los procesos han terminado")