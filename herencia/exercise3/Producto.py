# Clase base Producto
class Producto:
    # Constructor con nombre y precio
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Representación en texto
    def __str__(self):
        return f"Producto: {self.name}, Precio: {self.price}"
    
    # Calcula precio por cantidad
    def calculate_price(self, quantity):
        return self.price * quantity
    
    # Menor que, para ordenar por precio
    def __lt__(self, other):
        return self.price < other.price
