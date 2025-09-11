class Cliente:
    def __init__( self, i, n, e, f ):
        self.set__id (i)
        self.set__nome (n)
        self.set__email (e)
        self.set__fone (f)
    def get__id ( self ): return self.__id
    def get__nome ( self ): return self.__nome
    def get__email ( self ): return self.__email
    def get__fone ( self ): return self.__fone
    def set__id ( self, id ):
        if len(str(id)) > 4: raise ValueError("ID inválido")
        self.__id = id
    def set__nome ( self, nome ):
        if len(nome) < 3 or nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set__email ( self, email ):
        if len(email) < 5: raise ValueError("E-mail inválido")
        self.__email = email
    def set__fone ( self, fone ):
        if len(fone) < 4: raise ValueError("Telefone inválido")
        self.__fone = fone
    def __str__( self ): return f"{self.__id}: nome {self.__nome} - email {self.__email} - fone {self.__fone}"

class ClienteUI:
    __objetos = []
    @classmethod
    def main (cls):
        loop = 7
        while loop != 0:
            print(" ")
            match loop:
                case 1: ClienteUI.Abrir()
                case 2: ClienteUI.Listar()
                case 3: ClienteUI.Listar_id()
                case 4: ClienteUI.Atualizar()
                case 5: ClienteUI.Excluir()
                case 6: ClienteUI.Salvar()
                case 7: ClienteUI.Inserir()
            loop = ClienteUI.menu()

    @classmethod
    def menu ( cls ):
        print("0- Finalizar, 1- Abrir , 2- Listar, 3- Listar ID, 4- Atualizar, 5- Excluir, 6- Salvar, 7- Inserir")
        return int(input())
    
    @classmethod
    def Inserir (cls):
        id = int(input("Insira o ID: "))
        nome = input("Insira o nome: ")
        email = input("Insira o e-mail: ")
        fone = input("Insira o telefone: ")
        new = Cliente( id, nome, email, fone )
        cls.__objetos.append(vars(new))
        print("Inserido com sucesso!")

    @classmethod
    def Listar(cls):
        for i in cls.__objetos:
            print(i)

    @classmethod
    def Listar_id(cls):
        id, value = int(input("Insira o ID: ")), False
        for i in cls.__objetos:
            if i.get__id() == id:
                value, objeto = True, i
        if value: print(objeto)
        else: print("ID não encontrado")

    @classmethod
    def Atualizar(cls):
        id, value = int(input("Insira o ID a modificar: ")), False
        for i in cls.__objetos:
            if i.get__id() == id:
                value, objeto = True, i
        if value or objeto != any: 
            nome = input(f"Insira o novo nome[{objeto.get__nome()}]: ")
            email = input(f"Insira o novo e-mail[{objeto.get__email()}]: ")
            fone = input(f"Insira o novo telefone[{objeto.get__fone()}]: ")
            new = Cliente( id, nome, email, fone )
            cls.__objetos.remove(objeto)
            cls.__objetos.append(vars(new))
            print("Atualizado com sucesso!")
        else: print("ID não encontrado")    

    @classmethod
    def Excluir(cls):
        id, value = int(input("Insira o ID a modificar: ")), False
        for i in cls.__objetos:
            if i.get__id() == id:
                value, objeto = True, i
        if value or objeto != any: 
            cls.__objetos.remove(objeto)
            print("Excluído com sucesso!")
        else: print("ID não encontrado")

    @classmethod
    def Abrir(cls):
        print("Vazio")

    @classmethod
    def Salvar(cls):
        print("Salvo com sucesso!")
    
ClienteUI.main()