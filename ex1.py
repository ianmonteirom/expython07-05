"""
1. Preencha uma matriz 3x5 com números inteiros informados pelo usuário e exiba a matriz.
"""

matriz, linha = [], []
for i in range(3):
    linha = []
    for j in range(5):
        n = int(input('Número: '))
        linha.append(n)
    matriz.append(linha)

for i in range(3):
    for j in range(5):
        print(matriz[i][j], end='\t')
    print()
