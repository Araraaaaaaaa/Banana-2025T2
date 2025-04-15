'''Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores
podem ser números reais. Mostrar o resultado com duas casas decimais.
Digite a base e a altura do retângulo
3
4
Área = 12.00 - Perímetro = 14.00 - Diagonal = 5.00'''
import math 

base , altura = float(input("Base do retângulo = ")), float(input("Altura do retângulo = "))
Area, Peri, Diago = (base*altura) , ((altura*2)+(base*2)) , math.sqrt(base**2+altura**2)
print(f"Área = {Area} - Perímetro = {Peri} - Diagonal = {Diago}")
