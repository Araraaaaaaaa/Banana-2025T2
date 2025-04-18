'''https://www.beecrowd.com.br/repository/UOJ_1930.html'''
def funcionOfBanana(Tomadas, emp1, emp2, emp3):
    for indice, valor in enumerate(Tomadas):
        if emp1 != 0 and empty2 != 0 and empty3 != 0:
            T1, T2, T3, T4 = int(Tomadas[:emp1-1]), int(Tomadas[emp1+1:empty2-1]), int(Tomadas[empty2+1:empty3-1]), int(Tomadas[empty3+1:])
        if valor == " ":
            if emp1 == 0:
                emp1 = indice
            elif empty2 == 0:
                empty2 = indice
            elif empty3 == 0:
                empty3 = indice
Tomad, empty1, empty2, empty3 = str(input()), 0, 0, 0
 
print((T1-1)+(T2-1)+(T3-1)+T4)