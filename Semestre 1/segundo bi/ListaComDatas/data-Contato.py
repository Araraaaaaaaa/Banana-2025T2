from datetime import datetime
class Contato:
    def __init__(self, i, n, e, f, idad):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__idade = datetime.strptime(idad, "%d/%m/%Y" )
    def get_id(self): return self.__id    
    def get_nome(self): return self.__nome    
    def get_idade(self): return self.__idade
    def __str__(self): return f"{self.__nome}: {self.__id} - {self.__idade} - {self.__fone} - {self.__email}"

class ContatoUI:
    __contatos = []

    @classmethod    
    def main(cls):
        op = 0
        while op != 7:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniversariantes()

    @classmethod    
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversários, 7-Fim")
        return int(input("Escolha uma opção: "))
    
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
            #print(c)
            print(c.get_nome(),": ", c.get_id())

    @classmethod    
    def listar_id(cls, id):
        for c in cls.__contatos:
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
        else: cls.__contatos.remove(c)
    
    @classmethod    
    def pesquisar(cls):
        nome = input("Informe o nome: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês: "))
        print(f"Aniversariantes do mês de {mes}: ", end= "")
        for c in cls.__contatos:
            if c.get_idade().month == mes:        
                print (f"{c.get_nome()} faz aniversário dia {c.get_idade().day} do mês{c.get_idade().month}")

ContatoUI.main()