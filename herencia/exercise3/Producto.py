class Producto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Producto: {self.name}, Precio: {self.price}"
    
    def calculate_price(self, quantity):
        return self.price * quantity
    
    def __lt__(self, other):
        return self.price < other.price
