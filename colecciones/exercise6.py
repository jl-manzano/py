# Escribe un programa que tome una cadena de texto 
# como entrada y genere un diccionario que cuente la 
# frecuencia de cada palabra en el texto.
text = input("Enter a text:")
words = text.split()
frecuencia = {}
for word in words:
    word = word.lower()
    if word in frecuencia:
        frecuencia[word] += 1
    else:
        frecuencia[word] = 1
print(frecuencia)