class Viagem:
    def __init__( self , destin, distan, litros):
        self.set__destino( destin )
        self.set__distancia( distan )
        self.set__litros( litros )

    def get__destino ( self ): return self.__destino
    def get__distancia ( self ): return self.__distancia
    def get__litros ( self ): return self.__litros
    def set__destino ( self , destino):
        if destino == "": raise ValueError("Destino Inválido")
        self.__destino = destino
    def set__distancia ( self , distancia):
        if distancia <= 0: raise ValueError("Distância Inválido")
        self.__distancia = distancia
    def set__litros ( self , litros):
        if litros <= 0: raise ValueError("Litros Inválido")
        self.__litros = litros
    def Consumo ( self ): 
        if (self.__distancia / self.__litros) > self.__litros: return f" {(self.__distancia / self.__litros) - self.__litros} litros a mais do que tem no tanque"
        else: return f"{self.__distancia / self.__litros} do tanque"

    def __str__ ( self ): return f"Viagem - destino = {self.get__destino()} | distancia = {self.get__distancia()}KM | litros = {self.get__litros()}L"

class ViagemUI:
    def menu():
        print ("Selecione algum dos números para prosseguir -> 1 – Calcular viagem, 2 – Fim do programa")
        return int(input())
    @staticmethod
    def main():
        valor = 0
        while valor != 2:
            valor = ViagemUI.menu()
            match valor:
                case 1: ViagemUI.calculo()
                case 2: break
    def calculo():
        soft = Viagem(str(input("Seu destino('')-> ")), float(input("A distancia(KM)-> ")), float(input("Gasolina(L)-> ")))
        print("")
        print ( soft )
        print(f"Consumirá - {soft.Consumo()} ")
        print("")
User = ViagemUI()
User.main()