'''3. Retornar as iniciais do nome de uma pessoa dado seu nome completo, usando a função Iniciais abaixo. O
programa deve solicitar do usuário seu nome completo e mostrar as iniciais obtidas pela função.
def iniciais(nome)'''

def iniciais(nome):
    palavras = nome.split()
    iniciais = ""
    for i in palavras:
        if i[:1] != "d":
            iniciais = iniciais + " " + i[:1]
    return iniciais
print(iniciais(input()))