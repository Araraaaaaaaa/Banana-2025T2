'''https://www.beecrowd.com.br/repository/UOJ_1044.html'''

valores = input()
val = valores.split()
A, B = int(val[0]), int(val[1])
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")