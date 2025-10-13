# Implementa un programa que lea del fichero los datos, muestre los 
# nombres y calcule la media de la edad y de las estaturas, mostrándolas por pantalla.
<<<<<<< HEAD
# Abrimos archivo en modo lectura
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise1\\Alumnos.txt', 'rt')

# Leemos línea a línea y las mostramos
for linea in f.readlines():
    print(linea, end='')

# Cerramos el fichero (error: faltan paréntesis)
f.close
=======
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise1\\Alumnos.txt', 'rt')
for linea in f.readlines():
    print(linea,end = '')

f.close
>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
