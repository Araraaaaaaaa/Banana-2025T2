'''1. Retornar o maior entre dois números, usando a função Maior abaixo. O programa deve solicitar do usuário dois
valores e mostrar o maior valor entre eles utilizando a função Maior, que deve ser também implementada.
def maior(x, y)'''

def maior(Xa, Ya):
    if Xa > Ya:
        return(Xa)
    else:
        return(Ya)
Xe, Ye = int(input()), int(input())
print(f"O maior é o número {maior(Xe, Ye)}")