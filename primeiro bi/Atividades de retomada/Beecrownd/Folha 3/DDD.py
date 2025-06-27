'''https://www.beecrowd.com.br/repository/UOJ_1050.html'''

DDD = {61: "Brasília", 71: "Salvador", 11: "São Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora", 19: "Campinas", 27: "Vitoria", 31: "Belo Horizonte"}
DesejoDeMeninas = int(input())
if DesejoDeMeninas in DDD:
    print(DDD[DesejoDeMeninas])
else:
    print("DDD não cadastrado")