# Crea una clase llamada Articulo con los siguientes atributos: nombre, precio 
# (sin IVA), iva (siempre será 21) y cuantosQuedan (representa cuántos quedan en el almacén).
# Añade los siguientes métodos:
# Constructor con 3 parámetros que asigne valores a nombre, precio y cuantosQuedan. 
# El IVA siempre lo pondrá a 21.
# Método getPVP que devuelva el precio de venta al público (PVP) con iva incluido. 
# Método getPVPDescuento que devuelva el PVP con un descuento pasado como argumento. 
# Método vender que actualiza los atributos del objeto tras vender una cantidad ‘x’ 
# (si es posible). Devolverá true si ha sido posible (false en caso contrario). 
# La cantidad a vender se pasará como argumento al método.
# Método almacenar que actualiza los atributos del objeto tras almacenar una 
# cantidad ‘x’. La cantidad a almacenar se pasará como argumento.
# Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos artículos son iguales si tienen el mismo nombre. 
# Los artículos se ordenarán de menor a mayor por el nombre.
# Clase que representa un artículo de almacén
class Articulo:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    # Precio con IVA
    def getPVP(self):
        return self.price * (1 + Articulo.VAT / 100)
    
    # Precio con descuento
    def getPVPDescuento(self, discount):
        pvp = self.getPVP()
        return pvp * (1 - discount / 100)
    
    # Vender una cantidad
    def vender(self, quantity):
        res = True
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            res = False
        return res
    
    # Añadir al stock
    def almacenar(self, quantity):
        self.stock += quantity

    # Representación en string
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, VAT: {Articulo.VAT}, Stock: {self.stock}"
    
    # Comparar si son iguales (por nombre)
    def __eq__(self, other):
        return self.name == other.name
    
    # Ordenar por nombre
    def __lt__(self, other):
        return self.name < other.name