from Animal import Animal

class Gato(Animal):
    def __init__(self, name, count_legs):
        super().__init__(name, 4)
    
    def habla(self):
        return ' Miau'
    
    def __str__(self):
        return f"Soy un gato. {super().__str__()}"