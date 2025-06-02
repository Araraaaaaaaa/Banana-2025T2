import math
class equacao:
    def __init__( self , A, B, C):
        self.set__A( A )
        self.set__B( B )
        self.set__C( C )
    def set__A ( self, A ):
        if A == 0: raise ValueError("O primeiro valor não pode ser negativo")
        self.__A = A
    def set__B ( self, B ): self.__B = B
    def set__C ( self, C ): self.__C = C
    def get__A ( self ): return self.__A
    def get__B ( self ): return self.__B
    def get__C ( self ): return self.__C
    def Delta ( self ): return (self.__B**2)*(-4*self.__A*self.__C)
    def temRaizReal( self ):
        if self.Delta() >= 0: return True
        else: return False
    def R1 ( self ): return (-self.__B - (math.sqrt(self.Delta())))/2* self.__A
    def R2 ( self ): return (-self.__B + (math.sqrt(self.Delta())))/2* self.__A
    def __init__ ( self ):
        return f"Valores - A = {self.__A} | B = {self.__B} | C = {self.__C}"
        
class UI:
    def main():
        X, Y, Z, l = float(input("Qual o valor de A? ")), float(input("Qual o valor de B? ")), float(input("Qual o valor de C? ")), 10
        H = equacao( X, Y, Z )
        
        while l != 0:
            print("  ")
            print("0- encerrar | 1- Raiz tipo 1 | 2- Raiz tipo 2 | 3- Mudar valores | 4- Tipo da Raiz | 5- Delta | 6- Atributos")
            l = int(input())
            match l:
                case 1: H.R1()
                case 2: H.R2()
                case 3: 
                    H.set__A(float(input(f"Qual o novo valor de A [{H.get__A()}]? ")))
                    H.set__B(float(input(f"Qual o novo valor de B [{H.get__B()}]? ")))
                    H.set__C(float(input(f"Qual o novo valor de C [{H.get__C()}]? ")))
                case 4: print(f"A afirmação de que as raizes são reais é {H.temRaizReal()}")
                case 5: H.Delta()
                case 6: print(H)
                case 0: break;  
UI.main()