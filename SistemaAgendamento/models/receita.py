from models.DAO import DAO
from datetime import datetime
import json

class Receita:
    def __init__(self,idR, id_medicamento, id_profissional, id_cliente, periodo, dosagem, validade):
        self.set_id(idR)
        self.set_id_medicamento(id_medicamento)
        self.set_id_profissional(id_profissional)
        self.set_id_cliente(id_cliente)
        self.set_periodo(periodo)
        self.set_dosagem(dosagem)
        self.set_validade(validade)

    def get_id(self): return self.__id
    def get_id_medicamento(self): return self.__id_medicamento
    def get_id_profissional(self): return self.__id_profissional
    def get_id_cliente(self): return self.__id_cliente
    def get_periodo (self): return self.__periodo
    def get_dosagem (self): return self.__dosagem
    def get_validade (self): return self.__validade

    def set_id(self, id): self.__id = id
    def set_id_medicamento(self, id_medicamento): self.__id_medicamento = id_medicamento
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_periodo(self, periodo): #ex. "A cada 3 dias durante 3 meses"
        if periodo <= 0: raise ValueError("Periodo inválido")
        self.__periodo = periodo
    def set_dosagem(self, dosagem): #ex. 1 gota
        if dosagem == "": raise ValueError("Nome do medicamento inválido")
        self.__dosagem = dosagem
    def set_validade(self, validade):
        if validade < datetime.timedelta(2025, 1, 1): raise ValueError("Data inválida")
        self.__validade = validade

    def to_df(self): return {"id": self.__id, "validade": self.__validade}
    def to_json(self): return {"id": self.__id, "id-medicamento": self.__id_medicamento, "id-profissional": self.__id_profissional, "id-cliente": self.__id_cliente, "periodo": self.__periodo, "dosagem": self.__dosagem, "validade": self.__validade}
    @staticmethod
    def from_json(dic): return Receita(dic["id"], dic["id-medicamento"], dic["id-profissional"], dic["id-cliente"], dic["periodo"], dic["dosagem"], dic["validade"])
    def __str__(self): return f"{self.__id} - {self.__periodo} - {self.__dosagem} - {self.__validade}"

class ReceitaDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("receita.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Receita.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError: pass

    @classmethod
    def salvar(cls):
        with open("receita.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Receita.to_json)