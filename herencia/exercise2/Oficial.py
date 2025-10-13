# Importamos Operario
from Operario import Operario

# Oficial hereda de Operario
class Oficial(Operario):
    # Constructor
    def __init__(self, name):
        super().__init__(name)
    
    # __str__ extendido
    def __str__(self):
        return f"{super().__str__()} -> Oficial"
