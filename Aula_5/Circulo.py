class circulo:
    def __init__(self):
        self.raio = 1.2
        self.pi = 3.14
    def area (self):
        result = self.pi * self.raio**3
        return result
    def circuferencia(self):
        result = 2 * self.pi * self.raio
        return result
    
Y = circulo()
Y.raio = float(input())
Y.pi = 3.14
print(Y.area())
print(Y.circuferencia())
