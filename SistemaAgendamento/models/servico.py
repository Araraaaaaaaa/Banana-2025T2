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
    __coisas = []
    #.inserir
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        idd = 0
        if len(cls.__coisas) != 0:
            for aux in cls.__coisas:
                if aux.get_id() > idd: idd = aux.get_id()
        obj.set_id(idd + 1)
        cls.__coisas.append(obj)
        cls.salvar()
    #.listar
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__coisas
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__coisas:
            if obj.get_id() == id: return obj
        return None
    #.atualizar
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__coisas.remove(aux)
            cls.__coisas.append(obj)
            cls.salvar()
    #.excluir
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__coisas.remove(aux)
            cls.salvar()
    #.abrir
    @classmethod
    def abrir(cls):
        cls.__coisas = []
        try:
            with open("servico.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.__coisas.append(obj)
        except FileNotFoundError: pass

    #.salvar
    @classmethod
    def salvar(cls):
        with open("servico.json", mode="w") as arquivo:
            json.dump(cls.__coisas, arquivo, default = Servico.to_json)
