# Clases para demostración OOP
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre  
    
    def area(self):
        raise NotImplementedError("Método abstracto")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura