from datetime import datetime
class Paciente:
    def __init__( self, n, c, t, nasc): #nasc tem que ser uma tupla
        self.set_cpf(c)
        self.set_nome(n)
        self.set_telefone(t)
        self.set_nascimento(datetime(nasc))

    def get_cpf ( self ): return self.__cpf
    def get_nome ( self ): return self.__nome
    def get_telefone ( self ): return self.__telefone
    def get_nascimento ( self ): return self.__nascimento

    def set_cpf ( self , cpf):
        if len(cpf) != 11: raise ValueError("CPF inválido")
        self.__cpf = cpf
    def set_nome ( self , nome ):
        if len(nome) < 3: raise ValueError("Nome inválido")
        self.__nome = nome
    def set_telefone ( self , tele):
        if len(tele) != 10: raise ValueError("Formato de telefone inválido. (9XXXX-XXX)")
        self.__telefone = tele
    def set_nascimento ( self , nasci):
        if nasci > datetime.now(): raise ValueError("Pasciente ainda não nascido")
        self.__nascimento = nasci

    def Idade ( self ): 
        data = self.__nascimento - datetime.now()
        anos = data // 365
        meses = data % 365 // 30
        dias = data % 365 % 30
        return f"{anos} anos, {meses} meses e {dias} dias"
    
    def __str__( self ): return f"{self.__nome}: {self.__cpf} - {self.__nascimento} - {self.__telefone}"

class PacienteUI:
    pacientes = []
    manipulador = any

    def main (cls):
        loop = 8
        while loop != 0:
            match loop:
                case 1: PacienteUI.VerIdade()
                case 2: PacienteUI.VerCadastro()
                case 4: PacienteUI.Atualizar()
                case 8: PacienteUI.Criar()
            loop = PacienteUI.menu()

    def menu ( cls ):
        print("0- Finalizar, 1- Ver a Idade, 2- Ver cadastro, 4- Atualizar cadastro, 8- Criar cadastro")
        return int(input())
    
    def VerIdade ( cls ): 
        people = PacienteUI.pesquisa()
        if people == None: print("Paciente não encontrado")
        print(people.Idade())

    def VerCadastro ( cls ):
        people = PacienteUI.pesquisa()
        if people == None: print("Paciente não encontrado")
        print( people )

    def Atualizar ( cls ):
        people = PacienteUI.pesquisa()
        if people == None: print("Paciente não encontrado") 
        new = Paciente(people.get_cpf(), input(f"Informe o novo nome[{people.get_nome()}]: "), input(f"Informe o novo fone[{people.get_telefone()}]: "), input(f"Informe a nova data de nascimento[{people.get_nascimento()}]: "))
        cls.pacientes.remove(people)
        cls.pacientes.append(new)

    def Criar ( cls ):
        people = Paciente(int(input("Qual o cpf do novo paciente?[00000000000]")), str(input("Qual o nome do novo paciente?[xxx...]")), str(input("Qual o telefone do novo paciente?[9xxxx-xxxx]")), tuple(input("Qual a data de nascimento do novo paciente? [ano, mes, dia]")))
        cls.pacientes.append(people)

    def pesquisa ( cls ):
        PacienteUI.Listar()
        cpf = int(input("Qual o cpf do paciente?"))
        for people in cls.pacientes:
            if people.get_cpf == cpf: 
                return people
        return None
    
    def Listar ( cls ):
        if len(cls.historico) == 0: print("Nenhum paciente cadastrado")
        for c in cls.historico:
            print(c)