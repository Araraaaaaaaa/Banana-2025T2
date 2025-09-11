'''https://www.beecrowd.com.br/repository/UOJ_2424.html'''

corde = str(input())
cordenadas = corde.split()
X, Y = int(cordenadas[0]), int(cordenadas[1])
if X > 432 or X < 0 or Y < 0 or Y > 468:
    print("fora")
else:
    print("dentro")