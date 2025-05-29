class Frete:
    def __init__( self, distancia, peso ):
        self.set__distancia( distancia ) # self.__distancia = float
        self.set__peso( peso ) # self.__peso = float

    def set__distancia ( self, distancia ):
        if distancia <= 0 or distancia == "" : raise ValueError("Distancia não pode ser negativo ou nulo")
        self.__distancia = distancia
    def set__peso ( self, peso ):
        if peso <= 0 or peso == "" : raise ValueError("Peso não pode ser negativo ou nulo")
        self.__peso = peso
    def get__peso ( self ): return self.__peso
    def get__distancia ( self ): return self.__distancia
    def CalcFrete( self ): 
        return (0.01 * self.__peso) * self.__distancia
    
    def __str__( self ):
        return f"Frete -> Distancia = {self.get__distancia()} | Peso = {self.get__peso()}"

class UI:
    def main():
        D, P = float(input("Qual distância a ser percorrida? ")), float(input("Qual o peso da meradoria? "))  
        H = Frete( D, P )
        print("0- encerrar | 1- Mudar peso | 2- Mudar distancia | 3- Calcular frete | 4- Atributos")
        while l != 0:
            l = int(input())
            match l:
                case 1: H.set__peso(float(input(f"Mudar peso de {H.get__peso()} para: ")))
                case 2: H.set__distancia(float(input(f"Mudar distancia de {H.get__distancia()} para: ")))
                case 3: print(f"Valor do frete: {H.CalcFrete()}")
                case 4: print(H)
                case 0: break;  