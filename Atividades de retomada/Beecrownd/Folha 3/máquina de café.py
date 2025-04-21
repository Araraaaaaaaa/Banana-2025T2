'''https://www.beecrowd.com.br/repository/UOJ_2670.html'''

pessoas = []
for i in range(3):
    pessoas.append(int(input()))
ValorMax = max(pessoas)
for indic, value in enumerate(pessoas):
    if value == ValorMax:
        if indic == 0:
            tempo = pessoas[1] * 2 + pessoas[2] * 4
        elif indic == 1:
            tempo = pessoas[0] * 2 + pessoas[2] * 2
        elif indic == 2:
            tempo = pessoas[0] * 4 + pessoas[1] * 2
print(tempo)
