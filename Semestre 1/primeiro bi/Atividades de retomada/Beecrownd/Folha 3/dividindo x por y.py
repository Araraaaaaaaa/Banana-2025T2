'''https://www.beecrowd.com.br/repository/UOJ_1116.html'''

voltas = int(input())
for i in range(voltas):
    XeY = str(input())
    valores = XeY.split()
    X, Y = int(valores[0]), int(valores[1])
    if Y == 0:
        print("Divisão impossível")
    else:
        print(f"{X/Y:.1f}")