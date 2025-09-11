class Agua:
    def __init__(self):
        self.__mes = 1 #encapsulamento
        self.__ano = 2025
        self.__consumo = 0
    def set_mes(self, v): 
        if v < 1 or v > 12: raise ValueError("O mês deve estar entre 1 e 12.")
        self.__mes = v #método de acesso
    def set_ano(self, d):
        if d == 0 or d > 2025: raise ValueError("O ano não pode passar do atual e nem ser valor nulo.")
        self.__ano = d 
    def set_consumo(self, l): 
        if l < 0: raise ValueError("O consumo não pode ser negativo.")
        self.__consumo = l 
    def get_mes(self): return self.__mes
    def get_ano(self): return self.__ano
    def get_consumo(self): return self.__consumo

    def valor(self):
        if self.__consumo <= 10: return 38
        if 11 <= self.__consumo <= 20: return 38 + (self.__consumo - 10) * 5
        if self.__consumo > 20: return 38 + 50 + (self.__consumo - 20) * 6  

class Triangulo():
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2  

class UI: # UI = User Interface: print e input
    @staticmethod
    def menu():
        op = int(input("Informe uma opção: 1-Conta d'água, 2-Triângulo, 9-Fim: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
           # op = self.menu()
           op = UI.menu()
           if op == 1: UI.agua()
           if op == 2: UI.triangulo()
    @staticmethod
    def agua():
        x = Agua() # x é um objeto da classe Água
        x.set_mes (int(input("Informe o mês da conta: ")))
        x.set_consumo (int(input("informe o consumo em m3: ")))
        x.set_ano (int(input("informe o ano: ")))
        #Mes ano e consumo não são visíveis 
        print(f"O valor da conta de água do mês {x.get_mes} do ano {x.get_ano} é {x.valor()}")
    @staticmethod
    def triangulo():
        x = Triangulo() # x é um objeto da classe Triangulo
        x.b = int(input("Informe o valor da base: "))
        x.h = int(input("Informe o valor da altura: "))
        print(f"O triângulo de base {x.b} e altura {x.h} tem área {x.calc_area()}")

#x = UI()
#x.main()
UI.main()