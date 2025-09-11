class veloc_viagem:
    def __init__(self):
        self.KM = 1.9
        self.hora = 1
        self.minuto = 2
    def velocidade_m(self):
        self.minuto += self.hora * 60 #converte o item hora para minuto
        return self.minuto / self.KM
    
Y = veloc_viagem()
Y.KM, Y.hora, Y.minuto = 12, 2, 30
print(Y.velocidade_m())