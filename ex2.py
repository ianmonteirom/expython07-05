"""
2. Solicite ao usuário 12 valores e armazene em uma matriz 3x4 e exiba a matriz. A seguir, troque
todos os elementos da matriz que sejam maiores do que 100 pelo valor zero e exiba a matriz
novamente.
"""

matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        n = int(input('Número: '))
        linha.append(n)
    matriz.append(linha)

print('------ Matriz original: ------')
for i in range(3):
    for j in range(4):
        print(matriz[i][j], end='\t')
    print()

for i in range(3):
    for j in range(4):
        if matriz[i][j] > 100:
            matriz[i][j] = 0

print('------ Matriz nova (números maiores que 100 substituídos): ------')
for i in range(3):
    for j in range(4):
        print(matriz[i][j], end='\t')
    print()
