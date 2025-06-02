class equacao:
    def __init__( self , A, B, C):
        self.set__A( A )
        self.set__B( B )
        self.set__C( C )
    def set__A ( self, A ):
    def set__B ( self, B ):
    def set__C ( self, C ):
    def get__A ( self ): return self.__A
    def get__B ( self ): return self.__B
    def get__C ( self ): return self.__C
    def Delta ( self ):
    def temRaizReal( self ):
    def R1 ( self ):
    def R2 ( self ):
    def valores ( self ):
        X, Y, Z = float(input("Qual o valor de A? ")), float(input("Qual o valor de B? ")), float(input("Qual o valor de C? "))
        
class UI:
    def main():
        X, Y, Z, l = float(input("Qual o valor de A? ")), float(input("Qual o valor de B? ")), float(input("Qual o valor de C? ")), 10
        H = equacao( X, Y, Z )
        
        while l != 0:
            print("  ")
            print("0- encerrar | 1- Mudar valores | 2- Mudar distancia | 3- Calcular frete | 4- Atributos")
            l = int(input())
            match l:
                case 1: H.set__peso(float(input(f"Mudar peso de {H.get__peso()} para: ")))
                case 2: H.set__distancia(float(input(f"Mudar distancia de {H.get__distancia()} para: ")))
                case 3: print(f"Valor do frete: R${H.CalcFrete()}")
                case 4: print(H)
                case 0: break;  
UI.main()