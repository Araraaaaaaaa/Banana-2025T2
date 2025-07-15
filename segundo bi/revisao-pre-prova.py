from datetime import datetime

class Treino:
    def __init__(self, id, data, distan, tempI, tempF):
        self.set__id(id)
        self.set__data(datetime.strptime(data, "%d/%m/%Y"))
        self.set__distancia(distan)
        self.set__tempo(tempI, tempF)

    def get__id (self): return self.__id
    def get__data (self): return self.__data
    def get__distancia (self): return self.__distancia
    def get__tempo (self): return self.__tempo

    def set__id (self, id):
        if len(str(id)) != 4: raise ValueError("Id inválido. [XXXX]")
        self.__id = int(id)
    def set__data (self, data):
        if data > datetime.now(): raise ValueError("Um treino futuro não pode ser calculado")
        self.__data = data
    def set__distancia (self, distancia):
        if distancia <= 0: raise ValueError("Distância inesperada")
        self.__distancia = float(distancia)
    def set__tempo (self, tempoInit, tempoFin): #fazer a média para dar certo.
        tempo = datetime(tempoInit) - datetime(tempoFin, )
        if (tempo//60) <= 0: raise ValueError("Tempo inesperado")
        self.__tempo = tempo

    def __init__(self): return f"Treino {self.__id} de {datetime.strftime(self.__data, "%d/%m/%Y")} teve {self.__distancia} metros em {self.__tempo} "

class TreinoUI:
    __treinos = []
    @classmethod
    def main (cls):
        loop = 0
        while loop != 6:
            match loop:
                case 0: TreinoUI.inserir()
                case 1: TreinoUI.listar()
                case 2: TreinoUI.listar_id()
                case 3: TreinoUI.atualizar()
                case 4: TreinoUI.excluir()
                case 5: TreinoUI.MaisRapido()
            loop = TreinoUI.menu()

    @classmethod
    def menu (cls):
        print("0- inserir um novo treino, 1- listar todos os treinos, 2- listar um treino específico(id), 3- atualizar os dados de um treino, 4- excluir um treino, 5- encontrar o treino de maior velocidade, 6- sair;")
        return int(input("Escolha um ação: "))
    @classmethod
    def inserir (cls):
        new = Treino(int(input("Insira o id[0000]: ")), input("Data do treino[dia/mês/ano]: "),float(input("Insira a distância[M]: ")), input("Início do treino [H:Min:Sec]: "),input("Fim do treino [H:Min:Sec]: ") )
        cls.__treinos.append(new)

    @classmethod
    def listar (cls):
        for g in cls.__treinos:
            print(g.get__id(), ": ", g.get__data)

    @classmethod
    def listar_id (cls):
        id = int(input("Insira o ID: "))
        for g in cls.__treinos:
            if id == g.get__id:
                print(g)

    @classmethod
    def atualizar (cls):
        id = int(input("Insira o ID: "))
        for g in cls.__treinos:
            if id == g.get__id:
                new = Treino(id, input("Atualizar data[00/00/0000]: "),float(input("Atualizar a distância[M]: ")), input("Atualizar Tempo inicial do treino [00:00:00]: "), input("Atualizar Tempo final do treino [00:00:00]: ") )
                cls.__treinos.remove(g)
                cls.__treinos.append(new)
                print("Atualizado com sucesso!")
                
    @classmethod
    def excluir (cls):
        id = int(input("Insira o ID: "))
        for g in cls.__treinos:
            if id == g.get__id:
                cls.__treinos.remove(g)
                print("excluído com sucesso!")

    @classmethod
    def MaisRapido (cls):
        rapido = 0.00
        for value in cls.__treinos:
            if rapido <= value.get__tempo():
                texto = f"O treino {value.get__id()} foi o mais rápido com {value.get__distancia/value.get__tempo().second}"
        print(texto)