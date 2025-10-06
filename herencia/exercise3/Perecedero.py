from Producto import Producto

class Perecedero(Producto):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def __str__(self):
        return f"{super().__str__()}, Fecha de caducidad: {self.expiration_date}"
    
    def calculate_price(self, quantity):
        total_price = super().calculate_price(quantity)

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
