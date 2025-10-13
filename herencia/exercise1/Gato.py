# Importamos Animal
from Animal import Animal

# Clase Gato hereda de Animal
class Gato(Animal):
    # Constructor con 4 patas por defecto
    def __init__(self, name, count_legs):
        super().__init__(name, 4)
    
    # Método habla devuelve Miau
    def habla(self):
        return ' Miau'
    
    # Método __str__ personalizado
    def __str__(self):
        return f"Soy un gato. {super().__str__()}"
