'''https://www.beecrowd.com.br/repository/UOJ_1036.html | Dando resultados positivos'''
import math
AX2BXC = input()
valores = AX2BXC.split()
A, B, C = float(valores[0]), float(valores[1]), float(valores[2])
discriminante = (B**2+(-4*A*C))

if discriminante <= 0 or A == 0:
    print("Impossivel calcular")
else:
    print(f"X'  = {(B + (math.sqrt(discriminante)))/(A*2):.5f}")
    print(f"X'' = {(B - (math.sqrt(discriminante)))/(A*2):.5f}")