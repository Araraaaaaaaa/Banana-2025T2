import math 

base , altura = float(input("Base do retângulo = ")), float(input("Altura do retângulo = "))
Area, Peri, Diago = (base*altura) , ((altura*2)+(base*2)) , math.sqrt(base**2+altura**2)
print(f"Área = {Area} - Perímetro = {Peri} - Diagonal = {Diago}")
