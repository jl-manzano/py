# Importamos Empleado
from Empleado import Empleado

# Operario hereda de Empleado
class Operario(Empleado):
    # Constructor
    def __init__(self, name):
        super().__init__(name)
    
    # __str__ extendido
    def __str__(self):
        return f"{super().__str__()} -> Operario"
