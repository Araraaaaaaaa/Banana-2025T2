import math

class Retangulo:
    def __init__(self, base, height):
        # self.__base = float
        # self.__height = float
        self.set__base ( base )
        self.set__height ( height )
    def __str__( self ):
        return f"Triangulo -> base = {self.get__base()} | altura = {self.get__height()}"
    def set__base ( self, base ):
        if base <= 0: raise ValueError("Base não pode ser negativa")
        self.__base = base
    def set__height ( self, height):
        if height <= 0: raise ValueError("Altura não pode ser negativa")
        self.__height = height
    def get__base(self): return self.__base
    def get__height(self): return self.__height

    def CalcArea ( self ):
        return self.__base * self.__height / 2
    def CalcDiagonal ( self ):
        return math.sqrt(self.__base ** 2 + self.__height ** 2)
    
B , H= float(input("Qual a base do triângulo? ")), float(input("Qual a altura do triângulo? "))
J = Retangulo(B, H)
print(f"Area do triângulo = {J.CalcArea()}")
print(f"diagonal = {J.CalcDiagonal()}")
print(J)