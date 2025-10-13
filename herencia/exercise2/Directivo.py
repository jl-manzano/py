# Importamos Empleado
from Empleado import Empleado

# Directivo hereda de Empleado
class Directivo(Empleado):
    # Constructor
    def __init__(self, name):
        super().__init__(name)
    
    # __str__ extendido
    def __str__(self):
        return f"{super().__str__()} -> Directivo"
