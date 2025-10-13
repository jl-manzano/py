# Implementa un programa que lea del fichero los datos, muestre los 
# nombres y calcule la media de la edad y de las estaturas, 
# mostrándolas por pantalla.
<<<<<<< HEAD
# Abrimos archivo para escritura
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise2\\fichero.txt', 'w', encoding="utf8")

# Pedimos texto al usuario
linea = input("Introduce líneas de texto. Escribe 'fin' para terminar:")

# Mientras no escriba 'fin'
=======
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise2\\fichero.txt', 'w', encoding="utf8")

linea = input("Introduce líneas de texto. Escribe 'fin' para terminar:")

>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
while linea != "fin":
    f.write(linea + "\n")
    linea = input()

<<<<<<< HEAD
# Cerramos archivo
f.close()

# Confirmamos
print("\nLíneas almacenadas con éxito en 'fichero.txt'")
=======
f.close()

print("\nLíneas almacenadas con éxito en 'fichero.txt'")
>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
