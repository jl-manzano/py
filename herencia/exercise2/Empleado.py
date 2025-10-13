# Clase Empleado
class Empleado:
    # Constructor con nombre
    def __init__(self, name):
        self.name = name
    
    # Setter
    def setName(self, name):
        self.name = name

    # Getter
    def getName(self):
        return self.name
    
    # String representativo
    def __str__(self):
        return f"Empleado: {self.name}"
