class agua:
    def __init__(self): #init e self é para eclarar objetos, mas na class abaixo isso não acontece
        self.mes = 1
        self.ano = 2000
        self.consumo = 10
    def calculo(self):
        valor = 38
        if self.consumo >= 11 and self.consumo <= 20:
            valor = valor + (self.consumo - 10) * 5
        if self.consumo >= 21:
            valor = 88 + (self.consumo - 20) * 6
        return valor
    
class Interface:# ser Interface: print e input
    @staticmethod #permite chamar o def Main com a classe diretamente
    def menu():
        print(". ____________________________________ .")
        op = int(input("|1: Conta dágua    2: Encerrar programa|    Escolha sua ação: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 2 and op != 1:
            op = Interface.menu()
        if op == 1: Interface.agua()
    @staticmethod
    def agua():
        jorjinho = agua()
        jorjinho.consumo = int(input("Insira o seu consumo"))
        print(f"Usuário Jorjinho, o seu consumo de água no mês {jorjinho.mes} do ano de {jorjinho.ano} resulta numa cobrança de R${jorjinho.calculo():.2f}")
        Interface.main()

Interface.main()
  