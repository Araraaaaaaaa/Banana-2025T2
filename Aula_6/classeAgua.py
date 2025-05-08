class agua:
    def __init__(self):
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

jorjinho = agua()
jorjinho.consumo = int(input())
print(f"Usuário Jorjinho, o seu consumo de água no mês {jorjinho.mes} do ano de {jorjinho.ano} resulta numa cobrança de R${jorjinho.calculo():.2f}")