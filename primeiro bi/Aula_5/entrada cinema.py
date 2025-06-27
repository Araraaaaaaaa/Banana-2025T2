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
x = Ingresso()
x.dia, x.hora, J = str(input("Para qual dia? => ")), int(input("Para qual hora? => ")), str(input("Entrada inteira? (s/n) => "))

if J == "s": print(x.entrada_inteira())
else: print(x.entrada_meia())