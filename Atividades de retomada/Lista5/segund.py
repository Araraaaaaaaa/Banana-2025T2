'''2. Retornar o maior entre três números, usando a função Maior abaixo. O programa deve solicitar do usuário três
valores e mostrar o maior entre eles utilizando a função Maior, que deve ser também implementado.
def maior(x, y, z)'''

def maior (X, Y, Z):
    if X > Y and X > Z:
        return X
    elif Y > X and Y > Z:
        return Y
    elif Z > Y and Z > X:
        return Z

A, B, C = int(input()), int(input()), int(input())
print(f"O maior é o número {maior(A,B,C)}")