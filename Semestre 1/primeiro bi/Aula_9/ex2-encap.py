class conta_bancaria:
    def __init__(self):
        self.__titular = ""
        self.__Id = ""
        self.__saldo = 0.00
    # __________________________________________________________Encapsulamento_____________ #
    def set__Id ( self, id ):
        if id == "": raise ValueError ("id inválido")
        self.__Id = id
    def set__titular ( self, titular ):
        if titular == "": raise ValueError ("Nome inválido")
        self.__titular = titular
    def set__saldo ( self, saldo ):
        if not saldo >= 0 or saldo == "": raise ValueError ("Saldo inválido")
        self.__saldo = saldo
    def get__Id ( self ): return self.__Id
    def get__titular ( self ): return self.__titular
    def get__saldo ( self ): return self.__saldo
    # ____________________________________________________________________Operações__________ #
    def saque_saldo(self, menos): #não pode tirar mais do que você tem
        if self.__saldo < 0: raise ValueError ("Saldo negativo")
        if self.__saldo < menos: raise ValueError ("Saldo insuficiente")
        self.set__saldo (self.__saldo - menos)
        return self.__saldo 
    def deposito_saldo(self, mais):
        if mais <= 0: raise ValueError("Depósito não tem o valor mínimo")
        self.set__saldo(self.__saldo + mais)
        return self.__saldo
    
class interface:
    @staticmethod
    def main():
        X = conta_bancaria()
        X.set__titular (input("Qual seu nome? "))
        X.set__Id (input("Qual o seu id? "))
        X.set__saldo(float(input("Qual o seu saldo inicial? R$")))
        X.deposito_saldo(float(input("Faça seu primeiro depósito! => R$")))
        print(f"[!]          Titular {X.get__titular()} fez um depósito. Saldo atual = {X.get__saldo():.2f} reais")
        X.saque_saldo(float(input("Faça o seu primeiro saque! => ")))
        print(f"[!]          Titular {X.get__titular()} fez um saque. Saldo atual = {X.get__saldo():.2f} reais")

interface.main()