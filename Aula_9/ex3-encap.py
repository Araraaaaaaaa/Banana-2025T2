class Ingresso:
    def __init__(self):
        self.dia = "dom"
        self.hora = 18
    def entrada_inteira(self):
        if self.dia == "qua": valor = 8
        elif self.dia == "seg" or self.dia == "ter" or self.dia == "qui": valor = 16
        else: valor = 20
        if self.dia != "qua" and (self.hora >= 17 or self.hora == 0): valor = 1.5 * valor
        return valor
    def entrada_meia(self):
        if self.dia == "qua": valor = 8
        else: valor = self.entrada_inteira() / 2
        return valor
    
class interface():
    def menu():
        print("0-Finalizar programa; 1-Comprar um ingresso;")
        loop = 2
        while loop:
            escolha = int(input())
            if escolha < 0 and escolha > 1: Erase 
            match escolha:
                case 0: 
                case 1: interface.main()
    def main():
        x = Ingresso()
interface.menu()
# x.dia, x.hora, J = str(input("Para qual dia? => ")), int(input("Para qual hora? => ")), str(input("Entrada inteira? (s/n) => "))

# if J == "s": print(x.entrada_inteira())
# else: print(x.entrada_meia())