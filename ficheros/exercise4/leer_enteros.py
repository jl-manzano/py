# Implementa un programa que lea números enteros no ordenados de 
# un archivo, con un número por línea, y los almacene en una lista. 
# A continuación, debe guardar los números de la lista en otro fichero 
# distinto pero ordenados de forma ascendente.
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros.txt', 'rt')

enteros = []

for linea in f.readlines():
    try:
        enteros.append(int(linea.strip()))
    except:
        print(f"La línea '{linea.strip()}' no es un entero.")

enteros.sort()

f2 = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise4\\enteros_ordenados.txt', 'a')
for num in enteros:
    f2.write(f"{num}, ")

f.close