'''https://www.beecrowd.com.br/repository/UOJ_1930.html'''
Tomadas = input()
palavras = Tomadas.split()
T1, T2, T3, T4 = int(palavras[0]), int(palavras[1]), int(palavras[2]), int(palavras[3])
print((T1-1)+(T2-1)+(T3-1)+T4)