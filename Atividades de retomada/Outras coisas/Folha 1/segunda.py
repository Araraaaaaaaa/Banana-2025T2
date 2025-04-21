Nota1 = float(input("Nota do seu primeiro bimestre: "))
if Nota1 > 100 or Nota1 < 0:
    print("Valor inválido")
while Nota1 > 100 or Nota1 < 0:
    Nota1 = float(input("Nota do seu primeiro bimestre: "))

Nota2 = float(input("Nota do seu segundo bimestre: "))
if Nota2 > 100 or Nota2 < 0:
    print("Valor inválido")
while Nota2 > 100 or Nota2 < 0:
    Nota2 = float(input("Nota do seu segundo bimestre: "))

print(f"Média parcial do semestre = {(Nota1*2+Nota2*3)//5}")