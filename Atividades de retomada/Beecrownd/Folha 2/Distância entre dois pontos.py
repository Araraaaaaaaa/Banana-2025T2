'''https://www.beecrowd.com.br/repository/UOJ_1015.html || dando erro em todos os exemplos'''
import math
def funcionOfBanana(valores):
    for indice, valor in enumerate(valores):
        if valor == " ":
            X , Y = float(valores[:indice-1]), float(valores[indice+1:])
    print(X, Y)        
    return X, Y

lote1 , lote2 = str(input()) , str(input()) #não consegui puxar pelo input como float, estava dando o erro seguinte => ValueError: could not convert string to float: '1.0 7.0', pois, usando o exemplo do site -sem vírgulas-, o python não consegue diferenciar os termos
X1, Y1 = funcionOfBanana(lote1)
X2, Y2 = funcionOfBanana(lote2)
conta = math.sqrt((X2 - X1)**2+(Y2 - Y1)**2)
print(f"{conta:.4f}")