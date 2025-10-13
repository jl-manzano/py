# Escribe un programa que tome una cadena de texto 
# como entrada y genere un diccionario que cuente la 
# frecuencia de cada palabra en el texto.
# Pedimos texto
text = input("Enter a text: ")

# Separamos en palabras
words = text.split()

# Creamos diccionario vacío
frecuencia = {}

# Recorremos las palabras
for word in words:
    # Pasamos a minúsculas
    word = word.lower()
    # Si ya existe en el diccionario
    if word in frecuencia:
        # Aumentamos el contador
        frecuencia[word] += 1
    else:
        # Si no, la añadimos
        frecuencia[word] = 1

# Mostramos el diccionario final
print(frecuencia)
