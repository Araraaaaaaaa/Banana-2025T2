'''Ler uma frase com mais de uma palavra e mostrar sua última palavra (sem usar if – for – while – split). 
Digite uma frase:
Bem-vindo(a) ao Python
Python'''

S = input("Digite uma frase: ")
print(S [S.rindex(" ") + 1:])