'''1. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo(a) ao Python, <xxx>”, onde <xxx> é o
primeiro nome da pessoa.
Digite seu nome completo:
Gilbert Azevedo da Silva
Bem-vindo(a) ao Python, Gilbert'''

Nome = input("Qual o seu nome completo? ")
Name = Nome.split()
print(f"Bem-vindo(a) ao Python, {Name[0]}")