'''https://www.beecrowd.com.br/repository/UOJ_1015.html'''

import math
lote1 , lote2 = str(input()) , str(input()) #não consegui puxar pelo input como float, estava dando o erro seguinte => ValueError: could not convert string to float: '1.0 7.0', pois, usando o exemplo do site -sem vírgulas-, o python não consegue diferenciar os termos
lote1 , lote2 = lote1.split(), lote2.split()
X1, Y1, X2, Y2 = float(lote1[0]), float(lote1[1]), float(lote2[0]), float(lote2[1])

conta = math.sqrt((X2 - X1)**2+(Y2 - Y1)**2)
print(f"{conta:.4f}")