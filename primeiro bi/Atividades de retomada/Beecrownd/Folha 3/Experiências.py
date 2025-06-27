'''https://www.beecrowd.com.br/repository/UOJ_1094.html'''

Nesperimentos, coelhos, sapos, ratos = int(input()), 0, 0, 0
for i in range(Nesperimentos):
    entrada = str(input())
    entrada = entrada.split()
    match entrada[1]:
        case "C":
            coelhos += int(entrada[0])
        case "R":
            ratos += int(entrada[0])
        case "S":
            sapos += int(entrada[0])
total = coelhos + ratos + sapos
print(f"Total de cobaias: {total}")
print(f"Total de coelhos: {coelhos}", end=" | ")
print(f"Total de ratos: {ratos}", end=" | ")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos/total*100:.2f}%", end=" | ")
print(f"Percentual de ratos: {ratos/total*100:.2f}%", end=" | ")
print(f"Percentual de sapos: {sapos/total*100:.2f}%")