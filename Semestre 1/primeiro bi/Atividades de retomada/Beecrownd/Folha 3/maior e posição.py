'''https://www.beecrowd.com.br/repository/UOJ_1080.html'''

listoneta = []
for i in range(100):
    listoneta.append(int(input()))
for indic, value in enumerate(listoneta):
    if value == max(listoneta):
        print(max(listoneta))
        print(indic)
