from Animal import Animal

class Perro(Animal):
    def __init__(self, name, count_legs):
        super().__init__(name, 4)
    
    def habla(self):
        return ' Guau'
    
    def __str__(self):
        return f"Soy un perro. {super().__str__()}"