from Operario import Operario

class Oficial(Operario):
    def __init(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"{super().__str__()} -> Oficial"