class conta_bancaria:
    def __init__(self):
        self.titular = "Roberto"
        self.Id = 1000
        self.saldo = 0
    def saque_saldo(self, menos):
        if self.saldo < 0:   print("Em dívida com o banco. Impossível fazer saque.")
        else: 
            self.saldo -= menos
            print(f"Titular {self.titular} fez um saque. Saldo atual = {self.saldo:.2f} reais")
        return self.saldo
    def deposito_saldo(self, mais):
        self.saldo += mais
        print(f"Titular {self.titular} fez um depósito. Saldo atual = {self.saldo:.2f} reais")
        return self.saldo
X = conta_bancaria()
X.titular, X.Id, X.saldo = str(input("Qual seu nome? ")), int(input("Qual o seu id? ")), float(input("Qual o seu saldo inicial? "))

X.deposito_saldo(float(input("Faça seu primeiro depósito! =>")))
X.saque_saldo(float(input("Faça o seu primeiro saque! =>")))
