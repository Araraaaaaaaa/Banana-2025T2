class Retangulo :
    def __init__(self, b, a):
        self.A = a
        self.B = b
    def calc_area( self ):
        return self.B * self.A
    def calc_diagonal( self ):
        return (self.B ** 2 + self.A ** 2) **0.5
    def __str__( self ):
        return f"Base - {self.B}, Altura - {self.A}, Área - {self.calc_area()}, Diagonal - {self.calc_diagonal()}"
    