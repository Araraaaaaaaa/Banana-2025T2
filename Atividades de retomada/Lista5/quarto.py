'''4. Informar se um aluno foi aprovado ou está em prova final em uma disciplina, dadas as notas dos dois bimestres
de uma disciplina semestral, usando a função Aprovado abaixo. A função deve retornar verdadeiro quando o aluno
for aprovado (média >= 60) ou falso, caso contrário. O programa deve solicitar do usuário as notas dos dois
bimestres e mostrar a situação do aluno obtida pela função Aprovado.
def aprovado(nota1, nota2)'''

def aprovado(nota1, nota2):
    if (nota1+nota2)//2 >= 60:
        return True
    else:    
        return False
primeiro, segundo = int(input()), int(input())
if aprovado(primeiro, segundo) == True:
    print("Aprovado")
else:
    print("Em recuperação")