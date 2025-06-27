class Pais:
    def __init__( self ):
        self.id = int()
        self.nome = str()
        self.popu = int()
        self.area = float()
    def Pais(self, i, n, p, a): self.id, self.nome, self.popu, self.area = i, n, p, a
    def Densidade (self): return self.popu/self.area
    def __str__ ( self ): return f"{self.id} — {self.nome} | {self.popu} | {self.area} }"
class PaisUI: