# Implementa un programa que lea números enteros no ordenados de 
# un archivo, con un número por línea, y los almacene en una lista. 
# A continuación, debe guardar los números de la lista en otro fichero 
# distinto pero ordenados de forma ascendente.
<<<<<<< HEAD
# Abrimos archivo de lectura
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros.txt', 'rt')

# Lista para enteros
enteros = []

# Leemos línea a línea
=======
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros.txt', 'rt')

enteros = []

>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
for linea in f.readlines():
    try:
        enteros.append(int(linea.strip()))
    except:
        print(f"La línea '{linea.strip()}' no es un entero.")

<<<<<<< HEAD
# Ordenamos la lista
enteros.sort()

# Abrimos otro fichero para escribir
f2 = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros_ordenados.txt', 'a')

# Escribimos los números ordenados
for num in enteros:
    f2.write(f"{num}, ")

# Cerramos (error: faltan paréntesis)
f.close
=======
enteros.sort()

f2 = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros_ordenados.txt', 'a')
for num in enteros:
    f2.write(f"{num}, ")

f.close
>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
