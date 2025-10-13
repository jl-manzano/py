# Diseña una aplicación que pida al usuario su nombre y edad. 
# Estos datos deben guardarse en el fichero datos.txt. 
# Si este fichero existe, deben añadirse al final en una nueva línea, 
# y en caso de no existir, debe crearse.
<<<<<<< HEAD
# Abrimos archivo para añadir
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise3\\datos.txt', 'a', encoding="utf8")

# Pedimos nombre
nombre = input("Introduce tu nombre: ")

# Validamos edad
edad_valida = False
=======
f = open('C:\\Users\\jl.manzano\\Documents\\GitHub\\py\\ficheros\\exercise3\\datos.txt', 'a', encoding="utf8")
nombre = input("Introduce tu nombre: ")
edad_valida = False

>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
while not edad_valida:
    try:
        edad = int(input("Introduce tu edad: ").strip())
        edad_valida = True
    except:
        print("Por favor, introduce una edad válida.")

<<<<<<< HEAD
# Escribimos datos
f.write(f"{nombre}, {edad}\n")

# Confirmamos
print("\nDatos almacenados con éxito en 'datos.txt'")

# Cerramos
f.close()


=======
f.write(f"{nombre}, {edad}\n")
print("\nDatos almacenados con éxito en 'datos.txt'")
f.close()

>>>>>>> e7d2db3ce57d20ba6ca78955d31985630573f29f
