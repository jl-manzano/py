# Define una clase llamada Animal que tiene como atributos nombre y número de 
# patas. Además del constructor, define los siguientes métodos:
# habla: En la clase Animal devolverá una cadena vacía, ‘’.
# __str__: Devolverá una cadena de la siguiente forma: “Me llamo nombre, 
# tengo x patas y sueno así: sonido”. 
# Habrá que sustituir lo que está en azul por el nombre y el número de patas del animal. 
# En el caso de sonido hay que llamar a la función habla.
# A continuación, define dos clases, Gato y Perro que heredan de Animal. 
# En el caso de Gato, además del constructor, definirá los siguientes métodos:
# habla: Devolverá ‘Miau’.
# __str__: Primero escribirá “Soy un gato” y a continuación la misma cadena que 
# el padre.
# En el caso de Perro, además del constructor, definirá los siguientes métodos:
# habla: Devolverá “Guau”.
#__str__: Primero escribirá “Soy un perro” y a continuación la misma cadena que el padre.
# Creamos clase Animal
class Animal:
    # Constructor con nombre y patas
    def __init__(self, name, count_legs):
        self.name = name
        self.count_legs = count_legs

    # Método habla vacío
    def habla(self):
        return ''
    
    # Método para representar en string
    def __str__(self):
        return f"Me llamo {self.name}, tengo {self.count_legs} patas y sueno así: {self.habla()}"
