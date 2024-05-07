"""
3. Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, calcule o
somatório dos elementos da diagonal principal da matriz).
"""

from random import randint

matriz, diagprinc = [], []

for i in range(5):
    linha = []
    for j in range(5):
        n = randint(1, 99)
        linha.append(n)
        if i == j:
            diagprinc.append(n)
    matriz.append(linha)

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end='\t')
    print()

print(f'Somatório dos elementos da diagonal principal da matriz: {sum(diagprinc)}')
