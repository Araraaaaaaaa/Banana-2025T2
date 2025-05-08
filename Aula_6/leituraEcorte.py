frase, nova = input(), ""
for casa, lido in enumerate(frase):
    if lido == " ": nova = nova + " "
    else:
        if casa % 2 == 0: nova = nova + lido
print (nova)