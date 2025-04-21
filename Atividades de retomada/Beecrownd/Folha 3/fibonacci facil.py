'''https://www.beecrowd.com.br/repository/UOJ_1151.html'''

quantos, anterior, presente = int(input()), 0, 1
print(f"{anterior}  {presente}", end="  ")
for i in range(quantos-2):
    anterior, presente = presente, presente + anterior
    print(presente, end="  ")
     
    
