import json

class Cliente:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

def salvar():    #cria a pasta
    a = Cliente(1, "Alex")
    b = Cliente(2, "Danielle") 
    x = [a, b]
    with open("clientes.json", mode="w") as arquivo:
        json.dump(x, arquivo, default = vars)
    #arquivo.close()

def abrir():   #abre a pasta [o programa precisa ter criado a pasta]
    x = []
    with open("clientes.json", mode="r") as arquivo:
        lista = json.load(arquivo)
        for dic in lista:
            c = Cliente(dic["id"], dic["nome"])
            x.append(c)
    for c in x: print(c)

salvar()
            