import enum
from datetime import datetime

class Pagamento(enum.Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2

class Boleto:
    def __init__(self, valor, codigo, emissao, vencimento):
        self.set_tempo(datetime.strptime(emissao, "%d/%m/%Y"), datetime.strptime(vencimento, "%d/%m/%Y"))
        self.__situacao_pagamento = Pagamento.EmAberto
        self.__codBarras = codigo
        self.__valor_pago = 0.00
        self.set_boleto(valor)
        self.__dataPagto = None

    def get_situacao(self): return self.__situacao_pagamento
    def set_tempo (self, emissao, vencimento): #não permitir que a data de emissao seja maior que a data de vencimento
        if vencimento < emissao: raise ValueError("Emissão não pode ser após o vencimento.")
        self.__dataEmissao, self.__dataVencim = emissao, vencimento
    def set_boleto (self, valor):#não permitir que o valor pago seja nulo ou negativo
        if valor <= 0: raise ValueError("Valor de boleto inválido.")
        self.__valor_boleto = valor
        
    def pagar(self, valor_pago):
        if valor_pago <= 0: print("Valor de pagamento inválido.")
        else:
            self.__valor_pago += valor_pago
            if self.__valor_pago == self.__valor_boleto:
                self.__situacao_pagamento = Pagamento.Pago
                self.__dataPagto = datetime.strftime(datetime.now(), "%d/%m/%Y")
            else:
                self.__situacao_pagamento = Pagamento.PagoParcial
                self.__dataPagto = datetime.strftime(datetime.now(), "%d/%m/%Y")
            print("Pagamento realizado com sucesso!")

    def __str__ (self): return f"Boleto {self.__codBarras} com {self.__situacao_pagamento}. Vence em {self.__dataVencim.day}/{self.__dataVencim.month}/{self.__dataVencim.year} , emitido em {self.__dataEmissao.day}/{self.__dataEmissao.month}/{self.__dataEmissao.year}, pago em {self.__dataPagto} com {self.__valor_pago} reais."

class BoletoUI:
    @staticmethod
    def main():
        loop = 1
        while loop != 5:
            match loop:
                case 1: objeto = BoletoUI.formar_boleto()
                case 2: BoletoUI.informacoes(objeto)
                case 3: BoletoUI.pagamento(objeto)
                case 4: BoletoUI.situacao(objeto)
            loop = BoletoUI.menu()
    @staticmethod
    def menu():
        print("1- Formar boleto, 2- Resgatar informações, 3- Pagar boleto, 4- Ver situação, 5- Finalizar programa.")
        return int(input("Escolha uma ação: "))
    @staticmethod
    def formar_boleto():
        objeto = Boleto(float(input("Digite o valor do boleto: ")),
                        str(input("Digite o código de barras: ")),
                        str(input("Digite a data de emissão: ")),
                        str(input("Digite a data de vencimento: ")))
        return objeto  
    @staticmethod
    def informacoes (objeto):
        print(objeto)
    @staticmethod
    def pagamento(objeto):
        pagamento = float(input("Digite o valor do pagamento: "))
        objeto.pagar(pagamento)
    @staticmethod
    def situacao(objeto):
        print(objeto.get_situacao())

BoletoUI.main()