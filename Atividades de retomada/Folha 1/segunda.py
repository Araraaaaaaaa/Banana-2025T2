'''2. Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3).
Considerar as notas com valores inteiros entre zero e cem.
Digite a nota do primeiro bimestre da disciplina:
50
Digite a nota do segundo bimestre da disciplina:
70
Média parcial = 62'''

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