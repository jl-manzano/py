# Implementa un programa que lea números enteros no ordenados de 
# un archivo, con un número por línea, y los almacene en una lista. 
# A continuación, debe guardar los números de la lista en otro fichero 
# distinto pero ordenados de forma ascendente.
# Abrimos el archivo con los números originales en modo lectura
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros.txt', 'rt')

# Creamos una lista vacía para guardar los enteros
enteros = []

# Leemos todas las líneas del archivo
for linea in f.readlines():
    try:
        # Intentamos convertir cada línea a entero y añadirla a la lista
        enteros.append(int(linea.strip()))
    except:
        # Si hay una línea que no sea número, la mostramos
        print(f"La línea '{linea.strip()}' no es un entero.")

# Ordenamos la lista en orden ascendente
enteros.sort()

# Abrimos otro fichero para guardar los números ordenados
f2 = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros_ordenados.txt', 'a')

# Escribimos los números ordenados separados por comas
for num in enteros:
    f2.write(f"{num}, ")

# Cerramos los dos archivos correctamente
f.close()
f2.close()

# Confirmamos al usuario
print("Números ordenados guardados correctamente en 'enteros_ordenados.txt'")