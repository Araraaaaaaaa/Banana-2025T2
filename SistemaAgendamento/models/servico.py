from models.DAO import Manipulacao
import json

class Servico:
    def __init__(self, id, d, v):
        self.set_id(id)        
        self.set_descricao(d)
        self.set_valor(v)

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_descricao (self, descricao): self.__descricao = descricao
    def set_valor (self, valor): self.__valor = valor

    def to_df(self): return {"descricao":self.__descricao, "valor":self.__valor}
    def to_json(self): return {"id": self.__id, "descricao": self.__descricao, "valor": self.__valor}
    def from_json(dic): return Servico(dic["id"], dic["descricao"], dic["valor"])

    def __str__(self): return f"ID: {self.__id} - Valor: {self.__valor} - Descrição: {self.__descricao}"
    
class ServicoDAO:
    def inserir(obj): 
        ServicoDAO.abrir()
        Manipulacao.inserir(obj)
        ServicoDAO.salvar()
    def listar():
        ServicoDAO.abrir()
        Manipulacao.listar()
    def listar_id(id):
        ServicoDAO.abrir()
        Manipulacao.listar_id(id)
    def atualizar(id):
        Manipulacao.atualizar(id)
        ServicoDAO.salvar()
    def excluir(id):
        Manipulacao.excluir(id)
        ServicoDAO.salvar()

    def abrir():
        Manipulacao.objetos = []
        try:
            with open("servico.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    Manipulacao.objetos.append(obj)
        except FileNotFoundError: pass

    def salvar():
        with open("servico.json", mode="w") as arquivo:
            json.dump(Manipulacao.objetos, arquivo, default = Servico.to_json)