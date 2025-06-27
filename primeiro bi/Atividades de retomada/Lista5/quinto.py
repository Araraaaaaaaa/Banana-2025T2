'''5. Formatar o nome de uma pessoa deixando todas as letras iniciais em maiúsculo e as demais em minúsculo,
usando a função formatar_nome abaixo. O programa deve solicitar do usuário seu nome e mostrá-lo formatado.
def formatar_nome(nome)'''

'''def formatar_n(nome):
    nome, Chave, nome_format = nome.lower(), True, ''
    for valor in nome: # varre as letras
        if Chave:
            nome_format = nome_format + " " + valor.upper()
            Chave = False
        elif valor == " ":
            Chave = True
        else:
            nome_format = nome_format + valor
        
    return nome_format
print(formatar_n(input()))'''

'''Feito em sala:'''

def formatar_nome(name):
    name = name.lower()
    name = name.split()
    Resposta = ""
    for palavra in name:
        if palavra in ["da", "de", "e", "dos", "das", "do"]:
            Resposta = Resposta + palavra + " "
        else:
            Resposta = Resposta + (palavra[0].upper() + palavra[1:]) + " "
    return Resposta
print(formatar_nome(input("Digite o seu nome: ")))

