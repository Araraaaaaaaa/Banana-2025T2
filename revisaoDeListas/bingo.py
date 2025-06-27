import random
class Bingo:
    def __init__( self ):
        self.sorteados = []
        self.bolas = []
    def Iniciar ( self, numBolas ):
        if len(self.bolas) != 0: self.bolas.clear()
        if numBolas < 5: raise ValueError("Formato de bingo inválido")
        else:
            for boleta in range (1, numBolas+1, 1):
                self.bolas.append(boleta)
    def Sortear( self ):
        if len(self.bolas) == 0: raise ValueError("Jogo não iniciado")
        if len(self.bolas) == 0: return -1
        else: 
            sorte = self.bolas[random.randint(1, len(self.bolas))]
            self.sorteados.append(sorte)
            self.bolas.remove(sorte)
            return sorte
    def Sorteados( self ): return self.sorteados

class BingoUI:
    gordon = Bingo()

    @classmethod
    def Main(cls):
        loop = 9
        while loop != 0:
            loop = BingoUI.Menu()
            match loop:
                case 1: BingoUI.iniciarJogo()
                case 2: BingoUI.Sortear()
                case 3: BingoUI.Sorteados()
    @classmethod
    def Menu(cls):
        print("0-Sair, 1-Iniciar Jogo, 2-Sortear Número, 3-Números Sorteados")
        return int(input())
    @classmethod
    def iniciarJogo(cls): cls.gordon.Iniciar(int(input("Max bolas do bingo: ")))
    @classmethod
    def Sortear(cls):
        print("")
        print(f"{cls.gordon.Sortear()} acaba de ser sorteado!")
        print("")
    @classmethod
    def Sorteados(cls): print(f"sorteados: {cls.gordon.Sorteados()}")
BingoUI.Main()
