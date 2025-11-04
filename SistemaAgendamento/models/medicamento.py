from models.DAO import DAO
import json

class Medicamento:
    def __init__(self, id, nome, objetivo, aplicacao):
        self.set_id(id) #int
        self.set_nome(nome) 
        self.set_objetivo(objetivo)
        self.set_aplicacao(aplicacao) 

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_objetivo(self): return self.__objetivo
    def get_aplicacao(self): return self.__aplicacao

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): #ex. losartana
        if nome == "": raise ValueError("Nome do medicamento inválido")
        self.__nome = nome
    def set_objetivo(self, objetivo): # ex. tirar dor de cabeça e febre
        if objetivo == "": raise ValueError("Objetivo do medicamento inválido")
        self.__objetivo = objetivo
    def set_aplicacao(self, aplicacao): #via oral, injeção....
        if aplicacao == "": raise ValueError("Aplicação do medicamento inválida")
        self.__aplicacao = aplicacao

    def to_df(self): return {"nome": self.__nome, "aplicacao": self.__aplicacao, "objetivo": self.__objetivo}
    def to_json(self): return {"id": self.__id, "nome": self.__nome, "objetivo": self.__objetivo, "aplicacao": self.__aplicacao,}
    def from_json(self):
    def __str__(self):

class MedicamentoDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("medicamentos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Medicamento.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError: pass

    @classmethod
    def salvar(cls):
        with open("medicamentos.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Medicamento.to_json)