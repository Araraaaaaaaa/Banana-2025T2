'''5. Formatar o nome de uma pessoa deixando todas as letras iniciais em maiúsculo e as demais em minúsculo,
usando a função formatar_nome abaixo. O programa deve solicitar do usuário seu nome e mostrá-lo formatado.
def formatar_nome(nome)'''

def formatar_nome(nome):
    nome = nome.lower().split()
    for i in nome: # varre as palavras
        i[0] = i[0].upper()

    return nome
print(formatar_nome(input()))