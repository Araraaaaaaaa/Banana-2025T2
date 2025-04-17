'''https://www.beecrowd.com.br/repository/UOJ_2416.html || Dando erro no exemplo 2'''
Valores = str(input())
for indice, valor in enumerate(Valores):
    if valor == " ":
        Metros, Pista = int(Valores[:indice-1]), int(Valores[indice+1:])
print( Metros % Pista )