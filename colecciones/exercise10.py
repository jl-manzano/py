# Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
# El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. 
# Para ello, cada vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente 
# en el conjunto 2.
dictionary = {
    'e': 'p',
    'i': 'v',
    'k': 'i',
    'm': 'u',
    'p': 'm',
    'q': 't',
    'r': 'e',
    's': 'r',
    't': 'k',
    'u': 'q',
    'v': 's'
}

text = input("Enter a text: ").lower()
encrypted_text = ""

for letter in text:
    if letter in dictionary:
        encrypted_text += dictionary[letter]
    else:
        encrypted_text += letter
print(f"Encrypted text: {encrypted_text}")