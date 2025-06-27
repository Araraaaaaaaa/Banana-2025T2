class pais:
    def __init__ ( self , nom, pop, area):
        self.set__nome( nom )
        self.set__populacao( pop )
        self.set__area( area )

    def get__nome ( self ): return self.__nome
    def get__populacao ( self ): return self.__populacao
    def get__area ( self ): return self.__area
    def set__nome ( self, nome ):
        if len(nome) <= 2: raise ValueError("País inválido")
        self.__nome = nome
    def set__populacao ( self, populacao ):
        if populacao < 0: raise ValueError("População inválida")
        self.__populacao = populacao
    def set__area ( self, area ):
        if area <= 0.00: raise ValueError("Área inválida")
        self.__area = area 
    def densidade ( self ): return self.__populacao / self.__area

    def __str__( self ): return f"País - Nome = {self.__nome} | População = {self.__populacao} | Área = {self.__area}"

class paisUI:
    def menu():
        print ("Selecione algum dos números para prosseguir -> 1 – Calcular desidade demográfica, 2 – Fim do programa")
        return int(input())
    @staticmethod
    def main():
        valor = 0
        while valor != 2:
            valor = paisUI.menu()
            match valor:
                case 1: paisUI.calculo()
                case 2: break
    def calculo():
        soft = pais(str(input("Nome do País('')-> ")), int(input("A população(int)-> ")), float(input("A Área(float)-> ")))
        print("")
        print ( soft )
        print(f"Tem a densidade demográfica - {soft.densidade()}.")
        print("")
Cliente = paisUI
Cliente.main()