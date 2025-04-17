'''https://www.beecrowd.com.br/repository/UOJ_1015.html || dando erro em todos os exemplos'''
import math
def funcionOfBanana(valores):
    for indice, valor in enumerate(valores):
        if valor == " ":
            X , Y = float(valores[:indice-1]), float(valores[:indice-2])
    return X, Y

lote1 , lote2 = str(input()) , str(input()) #não consegui puxar pelo input como float, estava dando o erro seguinte => ValueError: could not convert string to float: '1.0 7.0'
X1, Y1 = funcionOfBanana(lote1)
X2, Y2 = funcionOfBanana(lote2)

print( math.sqrt(((X2-X1)**2)+((Y2-Y1)**2)) ) #não consigo colocar o :.4f