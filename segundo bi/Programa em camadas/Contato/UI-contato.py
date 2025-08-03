from views import ContatoVIEW

class ContatoUI:
    @staticmethod
    def main():
        op = 0
        while op != 10:
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.excluir()
            if op == 3: ContatoUI.abrir()
            if op == 4: ContatoUI.salvar()
            if op == 5: ContatoUI.atualizar()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.listar()
            if op == 8: ContatoUI.buscar_id()
            if op == 9: ContatoUI.aniversariantes()
            for one in range(3):
                print("")
            op = ContatoUI.menu()
            print("")

    @staticmethod    
    def menu():
        print("1-Inserir contato | 2-Listar contatos | 3-Buscar id | 4-Buscar nome | 5-Excluir contato | 6-Atualizar contato | 7-Aniversários | 8-Abrir backup | 9-Salvar alterções | 10-Fim")
        return int(input("Escolha uma opção: "))
    
    def inserir ():#inseri um contato a memória volátil, recebe str
        #gerar id
        result = ContatoVIEW.inserir( input("Informe o nome: ") , input("Informe o e-mail: "), input("Informe o fone: ") , input("Informe a data de nascimento: ") )
        print( result )

    @staticmethod    
    def excluir ():#excloi um contato, recebe str
        #ContatoUI.listar()
        result = ContatoVIEW.excluir( int(input("Informe o id do contato a ser excluído: ")) )
        print( result )

    @staticmethod    
    def abrir ():#abre o json, recebe list
        result = ContatoVIEW.abrir()
        try:
            for one in result: print( one )
        except:
            print("Sem backup disponível!")

    @staticmethod    
    def salvar (): #salva no json, recebe str
        print ( ContatoVIEW.salvar() )

    @staticmethod    
    def atualizar ():#modifica um usuário, recebe str
        #cls.listar()
        result = ContatoVIEW.atualizar( int(input("Informe o id do contato a ser atualizado: ")) )
        print ( result )

    @staticmethod    
    def pesquisar (): #pesquisa pelo nome, recebe str
        result = ContatoVIEW.pesquisar( int(input("Informe o nome do contato a ser pesquisado: ")) )
        print ( result )

    @staticmethod    
    def listar (): #apenas printa, recebe list
        print ( ContatoVIEW.listar() )
        
    @staticmethod
    def buscar_id (): #pesquisa id e printa, recebe str
        result = ContatoVIEW.pesquisar( int(input("Informe o id do contato a ser buscado: ")) )
        print ( result )

    @staticmethod    
    def aniversariantes():# mostra os aniversariantes do mês, recebe list ou none
        mes = int(input("Informe o mês: "))
        result = ( ContatoVIEW.aniversariantes( mes ) )
        print(f"Aniversariantes do mês de {mes}: ")
        if result == None: print(end = " Nenhum")
        else: 
            for one in result: print(one)

ContatoUI.main()