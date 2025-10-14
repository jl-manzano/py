# Importamos Operario
from Operario import Operario

# Tecnico hereda de Operario
class Tecnico(Operario):
    # Constructor
    def __init__(self, name):
        super().__init__(name)
    
    # __str__ extendido
    def __str__(self):
        return f"{super().__str__()} -> Tecnico"
