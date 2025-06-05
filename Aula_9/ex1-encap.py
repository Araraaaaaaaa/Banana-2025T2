class circulo:
    def __init__(self):
        self.__raio = 1.2
        self.__pi = 3.14
    def validar_raio(self, raio):
        if not raio > 0: raise ValueError
        self.__raio = raio
    def validar_pi(self, pi):
        if not pi >= 3 and pi <= 3.2: raise ValueError
        self.__pi = pi
    def pegar_raio(self): return self.__raio
    def pegar_pi(self): return self.__pi
    
    def area (self):
        result = self.__pi * self.__raio**3
        return result
    def circuferencia(self):
        result = 2 * self.__pi * self.__raio
        return result
    

class interface:
    @staticmethod
    def main():
        Y = circulo()
        Y.validar_raio ( float(input()) )
        Y.validar_pi ( 3.14 )
        print(f"Área do circulo {Y.area())}")
        print(Y.circuferencia())

interface.main()
