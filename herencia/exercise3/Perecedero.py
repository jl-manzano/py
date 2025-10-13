# Importamos Producto
from Producto import Producto

# Perecedero hereda de Producto
class Perecedero(Producto):
    # Constructor con fecha de caducidad
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    # Método __str__ ampliado
    def __str__(self):
        return f"{super().__str__()}, Fecha de caducidad: {self.expiration_date}"
    
    # Cálculo de precio según caducidad
    def calculate_price(self, quantity):
        total_price = super().calculate_price(quantity)

        # Ajustamos según días de caducidad
        match self.expiration_date:
            case 1:
                total_price /= 4
            case 2:
                total_price /= 3
            case 3:
                total_price /= 2
            case _:
                pass

        return total_price
