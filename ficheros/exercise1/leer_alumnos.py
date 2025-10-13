# Implementa un programa que lea del fichero los datos, muestre los 
# nombres y calcule la media de la edad y de las estaturas, mostrándolas por pantalla.
# Abrimos archivo en modo lectura
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise1\\Alumnos.txt', 'rt')

# Leemos línea a línea y las mostramos
for linea in f.readlines():
    print(linea, end='')

# Cerramos el fichero
f.close()