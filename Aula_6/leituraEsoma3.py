a, soma = input().split(), 0
for i in a: 
    if int(i) % 2 == 0: soma = soma + int(i)
print (f"Soma dos pares: {soma}")