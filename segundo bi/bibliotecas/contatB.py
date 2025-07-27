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

    def __str__(self): return f"{self.__nome}: {self.__id} - {datetime.strftime(self.__idade, "%d/%m")} - {self.__fone} - {self.__email}"

class ContatoUI:
    __contatos = []

    @classmethod    
    def main(cls):
        op = 1
        while op != 10:
            if op == 0: ContatoUI.assimilar()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.pesquisar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.atualizar()
            if op == 7: ContatoUI.aniversariantes()
            if op == 8: ContatoUI.abrir()
            if op == 9: ContatoUI.salvar()
            op = ContatoUI.menu()

    @classmethod    
    def menu(cls):
        print("0-Assimilar backup | 1-Inserir contato | 2-Listar contatos | 3-Buscar id | 4-Buscar nome | 5-Excluir contato | 6-Atualizar contato | 7-Aniversários | 8-Abrir backup | 9-Salvar alterções | 10-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod    
    def assimilar(cls):
        list = []
        with open("Contatos.json", mode = "r") as arquivo:
            dictmatriz = json.load(arquivo)
            for di in dictmatriz: #id, nome, email, fone, idade
                new = Contato(di["id"], di["nome"], di["email"], di["fone"], di["idade"])
                list.append(new)
        cls.__contatos.copy(list)

    @classmethod    
    def inserir(cls):
        id = ContatoUI.gerar_id()
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        idade = input("Informe a data de nascimento: ")
        c = Contato(id, nome, email, fone, idade)
        cls.__contatos.append(c)
        
    @classmethod   
    def gerar_id(cls):
        id = 0
        if len(cls.__contatos) == 0: return 1
        for c in cls.__contatos:
            if c.get_id() >= id:
                id = c.get_id() + 1
        return id
    
    @classmethod 
    def listar(cls):
        if len(cls.__contatos) == 0: print("Nenhum contato cadastrado")
        for c in cls.__contatos:
            print(c.get_nome(),": ", c.get_id())

    @classmethod    
    def listar_id(cls, id):
        for c in cls.__contatos:
            for k in c:
                if c.get_id() == id: return c
        return None    

    @classmethod    
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser atualizado: "))
        c = cls.listar_id(id)
        if c == None: print("Contato não encontrado")
        else:
            cls.__contatos.remove(c) 
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            fone = input("Informe o novo fone: ")
            idade = input("Informe o novo aniversário: ")
            c = Contato(id, nome, email, fone, idade)
            cls.__contatos.append(c)
            
    @classmethod    
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        c = cls.listar_id(id)
        if c == None: print("Contato não encontrado")
        else: 
            cls.__contatos.remove(c)
            print(f"{id} Removido com sucesso!")
    
    @classmethod    
    def pesquisar(cls):
        nome = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês: "))
        print(f"Aniversariantes do mês de {mes}: ")
        for c in cls.__contatos:
            if c.get_idade().month == mes:        
                print (f"{c.get_nome()} faz aniversário dia {c.get_idade().day} do mês {c.get_idade().month}")

    @classmethod
    def abrir(cls): #Abrir lê a lista de contatos de um arquivo;
        list = []
        with open("Contatos.json", mode = "r") as arquivo:
            dictmatriz = json.load(arquivo)
            for di in dictmatriz: #id, nome, email, fone, idade
                new = Contato(di["id"], di["nome"], di["email"], di["fone"], di["idade"])
                list.append(new)
        for i in list: print(i)

    @classmethod
    def salvar(cls): #Salvar grava a lista de contatos em um arquivo.
        with open("Contatos.json", mode ="w") as arquivo:
            json.dump( cls.__contatos, arquivo, default = Contato.convert)
        print("Progresso salvo!")

ContatoUI.main()