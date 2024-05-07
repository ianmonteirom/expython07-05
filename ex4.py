"""
4. Preencha uma matriz 5x5 com números aleatórios e exiba a matriz. A seguir, informe o menor
elemento da matriz.
"""

from random import randint

matriz, menor = [], 100

for i in range(5):
    linha = []
    for j in range(5):
        n = randint(1, 99)
        linha.append(n)
        if n < menor:
            menor = n
    matriz.append(linha)

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end='\t')
    print()

print(f'Menor elemento da matriz: {menor}')
