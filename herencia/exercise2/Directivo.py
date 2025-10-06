from Empleado import Empleado

class Directivo(Empleado):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"{super().__str__()} -> Directivo"