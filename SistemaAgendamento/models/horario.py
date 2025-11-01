from models.DAO import Manipulacao
from datetime import datetime
import json

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)
        self.set_id_profissional(0)

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    def set_id(self, id): self.__id = id
    def set_data(self, data): 
        if data < datetime.timedelta(2025, 1, 1): raise ValueError("Data inválida")
        self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_df(self):
        return {"data":self.__data, "confirmado":self.__confirmado}
    def to_json(self):
        return {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"), "confirmado":self.__confirmado, "id_cliente":self.__id_cliente,"id_servico":self.__id_servico, "id_profissional": self.__id_profissional}
    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_cliente(dic["id_cliente"])
        horario.set_id_servico(dic["id_servico"])
        horario.set_id_profissional(dic["id_profissional"])
        return horario

    def __str__(self): return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"

class HorarioDAO:
    def inserir(obj): 
        HorarioDAO.abrir()
        Manipulacao.inserir(obj)
        HorarioDAO.salvar()
    def listar():
        HorarioDAO.abrir()
        Manipulacao.listar()
    def listar_id(id):
        HorarioDAO.abrir()
        Manipulacao.listar_id(id)
    def atualizar(id):
        Manipulacao.atualizar(id)
        HorarioDAO.salvar()
    def excluir(id):
        Manipulacao.excluir(id)
        HorarioDAO.salvar()
    def listar_id_cliente(id_cliente):
        HorarioDAO.salvar()
        Manipulacao.listar_id_cliente(id_cliente)
    def listar_id_profissional(id_profissional):
        HorarioDAO.salvar()
        Manipulacao.listar_id_profissional(id_profissional)

    def abrir():
        Manipulacao.objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    Manipulacao.objetos.append(obj)
        except FileNotFoundError: pass

    def salvar():
        with open("horarios.json", mode="w") as arquivo:
            json.dump(Manipulacao.objetos, arquivo, default = Horario.to_json)