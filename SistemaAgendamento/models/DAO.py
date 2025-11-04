class Manipulacao:
    objetos = []

    @classmethod
    def listar_id_profissional(cls, id, tos):
        cls.objetos = tos
        lista = []
        for obj in Manipulacao.objetos:
            if obj.get_id_profissional() == id:
                lista.append(obj)
        return lista
    
    @classmethod
    def listar_id_cliente(cls, id, tos):
        cls.objetos = tos
        lista = []
        for obj in Manipulacao.objetos:
            if obj.get_id_cliente() == id:
                lista.append(obj)
        return lista
    
    @classmethod
    def inserir(cls, obj, tos):
        cls.objetos = tos
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id: 
                id= aux.get_id()
        obj.set_id(id+1)
        cls.objetos.append(obj)
        #cls.salvar()

    @classmethod
    def listar(cls, tos):
        cls.objetos = tos
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id, tos):
        cls.objetos = tos
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            #cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            #cls.salvar()