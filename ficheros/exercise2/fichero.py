# Implementa un programa que lea del fichero los datos, muestre los 
# nombres y calcule la media de la edad y de las estaturas, 
# mostrándolas por pantalla.
# Abrimos archivo para escritura
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise2\\fichero.txt', 'w', encoding="utf8")

# Pedimos texto al usuario
linea = input("Introduce líneas de texto. Escribe 'fin' para terminar:")

# Mientras no escriba 'fin'
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise2\\fichero.txt', 'w', encoding="utf8")

linea = input("Introduce líneas de texto. Escribe 'fin' para terminar:")

while linea != "fin":
    f.write(linea + "\n")
    linea = input()

# Cerramos archivo
f.close()

# Confirmamos
print("\nLíneas almacenadas con éxito en 'fichero.txt'")