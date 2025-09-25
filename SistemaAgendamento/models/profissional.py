import json

class Profissional:
    def __init__(self, id, n, e, c):
        self.set_id(id)
        self.set_nome(n)
        self.set_especialidade(e)
        self.set_conselho(c)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_especialidade(self, espe): self.__especialidade = espe
    def set_conselho(self, conse): self.__conselho = conse

    def to_json(self): return {"id": self.__id, "nome":self.__nome, "espec":self.__especialidade, "conselho": self.__conselho}
    def from_json(dic): return Profissional(dic["id"], dic["nome"], dic["espec"], dic["conselho"])
    def __str__(self): return f"{self.__nome} - {self.__id} {self.__especialidade} - {self.__conselho}"

class ProfissionalDAO:

    __pessoas = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        idddd = 0
        for aux in cls.__pessoas:
            if aux.get_id() > idddd: idddd = aux.get_id()
        obj.set_id(idddd +1)
        cls.__pessoas.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__pessoas

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__pessoas:
            if obj.get_id() == id: return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__pessoas.remove(aux)
            cls.__pessoas.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__pessoas.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__pessoas = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.__pessoas.append(obj)
        except FileNotFoundError: pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls.__pessoas, arquivo, default = Profissional.to_json)
