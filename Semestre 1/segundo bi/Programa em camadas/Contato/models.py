#apenas esse vai para a atividade
from datetime import datetime
import json

class Contato:
    def __init__(self, i, n, e, f, idad):
        self.set_id(i)
        self.set_nome(n)
        self.set_email(e)
        self.set_fone(f)
        self.set_idade(idad)

    def set_id ( self , ID):
        if len(str(ID)) > 5 or ID <= 0: raise ValueError("ID inválido. [x : xxxxx]")
        self.__id = ID
    def set_fone ( self , tele):
        if len(tele) != 10: raise ValueError("Formato de telefone inválido. [9XXXX-XXXX]")
        self.__fone = tele
    def set_nome ( self , nome ):
        if len(nome) < 3: raise ValueError("Nome inválido")
        self.__nome = nome
    def set_email ( self , email ):
        if len(email) < 6: raise ValueError("E-MAIL inválido. [@x.com]")
        self.__email = email
    def set_idade ( self, idade ):
        self.__idade = datetime.strptime(idade, "%d/%m")

    def get_id(self): return self.__id    
    def get_nome(self): return self.__nome  
    def get_idade(self): return self.__idade
    def get_fone(self): return self.__fone
    def get_email(self): return self.__email

    def convert (self):
        dicio = {}
        dicio["id"] = self.__id 
        dicio["nome"] = self.__nome
        dicio["email"] = self.__email
        dicio["fone"] = self.__fone
        dicio["idade"] = self.__idade.strftime("%d/%m")
        return dicio

    def __str__(self): return f"[{self.__nome}] - ID: {self.__id} - Nascimento: {datetime.strftime(self.__idade, "%d/%m")} - Telefone: {self.__fone} - E-mail: {self.__email}"

#aqui fica o enum

class ContatoDAO:
    __contatos = []

    @classmethod    
    def inserir(cls, nome, email, fone, idade):
        c = Contato(ContatoDAO.gerar_id(), nome, email, fone, idade)
        cls.__contatos.append(c)
        return "Inserido com sucesso!"
        
    @classmethod   
    def gerar_id(cls): #gera id, não printa ou passa a outras classes.
        id = 0
        if len(cls.__contatos) == 0: return 1
        for c in cls.__contatos:
            if c.get_id() >= id:
                id = c.get_id() + 1
        return id
    
    @classmethod
    def buscar_id(cls, id): #busca alguém pelo id
        value = False
        for i in cls.__contatos:
            if i.get_id() == id:
                value, objeto = True, i
        if value: return objeto
        else: return "ID não encontrado"

    @classmethod 
    def listar(cls): #mostra todos os contatos. retorna list 
        list = []
        if len(cls.__contatos) == 0: return "Nenhum contato cadastrado"
        for c in cls.__contatos:
            list.append(f"{c.get_nome()}:  {c.get_id()}")
        return list

    @classmethod    
    def listar_id(cls, id): #processo de procurar o sujeito, não printa
        for c in cls.__contatos:
            for k in c:
                if c.get_id() == id: return c
        return None    

    @classmethod    
    def atualizar(cls, id, nome, email, fone, idade): #modifica um sujeito já criado
        c = cls.listar_id(id)
        if c == None: return "Contato não encontrado" 
        else:
            cls.__contatos.remove(c) 
            c = Contato(id, nome, email, fone, idade)
            cls.__contatos.append(c)
            return "Atualizado com sucesso!"
            
    @classmethod    
    def excluir(cls, id): #exclui um sujeito
        cls.listar()
        c = cls.listar_id(id)
        if c == None: return "Contato não encontrado"
        else: 
            cls.__contatos.remove(c)
            return f"{id} Removido com sucesso!"
    
    @classmethod    
    def pesquisar(cls, nome): #pesquisa alguem a partir do nome
        pessoa = any
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): pessoa = c
        if pessoa == any: return "Nome não encontrado"
        else: return pessoa

    @classmethod
    def aniversariantes(cls, mes): #quais os aniversariantes do mês
        list = []
        for c in cls.__contatos:
            if c.get_idade().month == mes:        
                list.append(f"{c.get_nome()} faz aniversário dia {c.get_idade().day} do mês {c.get_idade().month}")
        return list
    
    @classmethod
    def abrir(cls): #lê o arquivo. model
        list = []
        try:
            with open("Contatos.json", mode = "r") as arquivo:
                dictmatriz = json.load(arquivo)
                for di in dictmatriz: #id, nome, email, fone, idade
                    new = Contato(di["id"], di["nome"], di["email"], di["fone"], di["idade"])
                    list.append(new)
            cls.__contatos = list.copy()
            return "Backup concluído!"
        except FileNotFoundError: return "Sem backup"

    @classmethod
    def salvar(cls): #grava a lista em um arquivo. model
        with open("Contatos.json", mode ="w") as arquivo:
            json.dump( cls.__contatos, arquivo, default = Contato.convert)
        return "Progresso salvo!"
