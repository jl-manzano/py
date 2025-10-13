# Importamos Producto
from Producto import Producto

# NoPerecedero hereda de Producto
class NoPerecedero(Producto):
    # Constructor con tipo
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    # Método __str__ ampliado
    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.type}"
    
    # Usa cálculo de la clase padre
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)
