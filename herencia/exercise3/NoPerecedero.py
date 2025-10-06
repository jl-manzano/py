from Producto import Producto

class NoPerecedero(Producto):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.type}"
    
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)
