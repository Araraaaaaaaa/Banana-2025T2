class circulo:
    def __init__(self):
        self.rao = 1.2
        self.pi = 3.14
    def area (self):
        return self.pi * self.rao**3
    def circuferencia(self):
        return 2 * self.pi * self.rao
    
Y = circulo
Y.rao = float(input())
print(Y.area,  Y.circuferencia)
