#from enum import Enum
class Idade:
    def __init__ ( self ):
        self.__binario = int( 0 )

    def Criar ( self, initial ): #cria as cartelas e seus números. Basicaente todos os números que podem ser formados por initial
        valores, flutuante = [initial], initial #flutuante não é float.
        # - - -(initial - 1 * 1 + initial + 1) - - - #
        while flutuante <= 127:
            if initial != 1: #quando initial não é 1 ele segue um pardão para a sucessão de números, segue uma sequência de somas de um que equivale a 1*initial-1 e em seguida tem um pulo de initial+1
                for b in range(initial - 1):
                    flutuante += 1
                    if flutuante > 127: return valores
                    valores.append(flutuante)
                flutuante += initial + 1
                if flutuante > 127: return valores
                valores.append(flutuante)
            else: #quando initial é 1 (1bin) os números seguintes pulam de 2 em 2
                flutuante += 2
                if flutuante > 127: return valores
                valores.append(flutuante)
        return valores
    
    def Contagem ( self, valores ):#converte a lista de s's ou n's resultante das perguntas sobre as cartelas em uma chave para adicionar ou não valores equivalentes a binário
        for endereco, value in enumerate(valores):
            if value == "s": #ex: self.__binario = 0
                self.__binario += (2 ** endereco) #ex:self.__binario = self.__binario + (2^(0)) -> self.__binario = 0 + 1
        return self.__binario #ex: self.__binario = 1

class idadeUI:
    cartelas = [1, 2, 4, 8, 16, 32, 64]
    separador = ""

    @classmethod
    def menu ( cls, sessao ):
        cartele = Idade()
        print(cls.separador)
        print ("A sua idade está na cartela seguinte? [s/n]")
        print(cartele.Criar(cls.cartelas[sessao]))
        return str(input())
    
    @classmethod
    def main( cls ):
        loop = 2
        while loop != 0:
            print("0- Finalizar, 1- Iniciar")
            print(cls.separador)
            loop = int(input())
            match loop:
                case 1: idadeUI.cont()

    @classmethod
    def cont ( cls ):
        sessao = 0
        jorge = Idade()
        escolha = []
        for k in range(len(cls.cartelas)):
            escolha.append(idadeUI.menu( sessao ))
            sessao += 1
        print(cls.separador)
        print (f"           Sua idade é {jorge.Contagem( escolha )}")
        print(cls.separador)

idadeUI.main()

'''class posicoes ( Enum ):
    primeira = 1
    segunda = 2
    terceira = 4
    quarta = 8
    quinta = 16
    sexta = 32
    setima = 64'''