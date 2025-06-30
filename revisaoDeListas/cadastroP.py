class PaisCadastro:
    def __init__( self ):
        self.id = int()
        self.nome = str()
        self.popu = int()
        self.area = float()
    def Pais(self, i, n, p, a): self.id, self.nome, self.popu, self.area = i, n, p, a
    def Densidade (self): return self.popu/self.area
    def __str__ ( self ): return f"{self.id} — {self.nome} | {self.popu} | {self.area}"

class PaisUI:
    paises = []
    @classmethod
    def main(cls):
        loop = 10
        while loop != 0:
            loop = PaisUI.menu()
            match loop:
                case 1: PaisUI.inserir()
                case 2: PaisUI.excluir()
                case 3: PaisUI.atualizar()
                case 4: PaisUI.listar()
                case 5: PaisUI.maisPopuloso()
                case 6: PaisUI.maisPovoado()
    @classmethod
    def menu(cls):
        print("0-sair, 1-Inserir, 2-excluir, 3-atualizar, 4-listar, 5-mais populoso, 6-mais povoado")
        return int(input())
    @classmethod
    def inserir (cls):
        novo = PaisCadastro()
        novo.Pais(int(input("Informe o id: ")), (input("Informe o nome: ")), int(input("Informe a população: ")), float(input("Informe a área: ")))
        cls.paises.append(novo)
    @classmethod
    def listar (cls):
        for i in cls.paises:
            print(i)
    @classmethod
    def atualizar (cls):
        id = int(input("Id a alterar: "))
        alter = PaisCadastro
        for i in cls.paises:
            if i.id == id:
                cls.paises.remove(i)
                alter.Pais(id , (input("Novo nome: ")), int(input("Nova população: ")), float(input("Nova área: ")))
                cls.paises.append(alter)
    @classmethod
    def excluir (cls):
        id = int(input("Id a alterar: "))
        for i in cls.paises:
            if i.id == id:
                cls.paises.remove(i)
    @classmethod
    def maisPopuloso (cls):
        outro = 0
        for j in cls.paises:
            if j.popu > outro:
                nome = j.nome
                outro = j.popu
        print(f"{nome} - {outro}")
    @classmethod
    def maisPovoado (cls):
        outro = 0
        for j in cls.paises:
            if j.Densidade() > outro:
                nome = j.nome
                outro = j.Densidade()
        print(f"{nome} - {outro}")
PaisUI.main()