# Importamos Animal
from Animal import Animal

# Clase Perro hereda de Animal
class Perro(Animal):
    # Constructor con 4 patas
    def __init__(self, name, count_legs):
        super().__init__(name, 4)
    
    # Método habla devuelve Guau
    def habla(self):
        return ' Guau'
    
    # Método __str__ personalizado
    def __str__(self):
        return f"Soy un perro. {super().__str__()}"