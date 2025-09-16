from datetime import datetime

class PPaciente:
    #______--__- Construtor
    def __init__( self, N, C, T, Nasc):
         self.set__nome(N)
         self.set__cpf(C)
         self.set__telefon(T)
         self.set__nascimento(Nasc)

    #______--__- Métodos de alteração e verificação dos atributos
    def set__nome (self, Xnome): 
        if len(Xnome) < 3: raise ValueError("Nome Inválido")
        else: self.__nome = Xnome
    def set__cpf (self, Xcpf): 
        if len(Xcpf) != 11 : raise ValueError("CPF Inválido")
        else: self.__cpf = Xcpf 
    def set__telefon (self, Xtelefon): 
        if len(Xtelefon) != 10 : raise ValueError("Número telefonico Inválido")
        else: self.__telefon = Xtelefon
    def set__nascimento (self, Xnascimento): 
        if datetime.now() > Xnascimento or datetime.now() != Xnascimento: raise ValueError("Data Inválida")
        self.__nascimento = Xnascimento
    
    #______--__- Métodos de recuperação dos atributos encapsulados
    def get__nome (self): return self.__nome
    def get__cpf (self): return self.__cpf
    def get__telefon (self): return self.__telefon
    def get__nascimento (self): return self.__nascimento

    #______--__- Método que informa a idade do paciente em relação ao agora
    def idade(self): 
        return f"Paciente: {self.__nome}, Anos: {self.__nascimento.days // 365}, Meses: {self.__nascimento.days % 365 // 30}, Dias: {self.__nascimento.days % 365 % 30},"

    #______--__- Informes gerais
    def __str__ (self):
        return f"Paciente: {self.__nome}, CPF: {self.__cpf}, Idade: {datetime.strftime(self.__nascimento)}, Contato: {self.__telefon}"