from models.DAO import Manipulacao
import json

class Profissional:
    def __init__(self, id, n, e, c, em, senha):
        self.set_id(id)
        self.set_nome(n)
        self.set_especialidade(e)
        self.set_conselho(c)
        self.set_email(em)
        self.set_senha(senha)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_senha(self): return self.__senha
    def get_email(self): return self.__email

    def set_email(self, email): 
        if email == "": raise ValueError("Email do profissional inválido")
        self.__email = email
    def set_senha(self, senha): 
        if senha == "": raise ValueError("Senha do profissional inválida")
        self.__senha = senha
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): 
        if nome == "": raise ValueError("Nome do profissional inválido")
        self.__nome = nome
    def set_especialidade(self, espe): self.__especialidade = espe
    def set_conselho(self, conse): self.__conselho = conse

    def to_df(self): return {"nome":self.__nome, "especialidade":self.__especialidade,"conselho":self.__conselho, "email":self.__email}
    def to_json(self): return {"id": self.__id, "nome":self.__nome, "espec":self.__especialidade, "conselho": self.__conselho, "email": self.__email, "senha": self.__senha}
    def from_json(dic): return Profissional(dic["id"], dic["nome"], dic["espec"], dic["conselho"], dic["email"], dic["senha"])
    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho} - {self.__email}"

class ProfissionalDAO:
    def inserir(obj): 
        Manipulacao.inserir(obj, ProfissionalDAO.abrir())
        ProfissionalDAO.salvar()
    def listar():
        return Manipulacao.listar(ProfissionalDAO.abrir())
    def listar_id(id):
        return Manipulacao.listar_id(id, ProfissionalDAO.abrir())
    def atualizar(id):
        Manipulacao.atualizar(id)
        ProfissionalDAO.salvar()
    def excluir(id):
        Manipulacao.excluir(id)
        ProfissionalDAO.salvar()

    def abrir():
        objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    objetos.append(obj)
        except FileNotFoundError: pass
        return objetos

    def salvar():
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(Manipulacao.objetos, arquivo, default = Profissional.to_json)