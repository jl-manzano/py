from Operario import Operario

class Tecnico(Operario):
    def __init(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"{super().__str__()} -> Tecnico"