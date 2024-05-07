"""
5. Preencha uma matriz 5x4 com números informados pelo usuário e exiba a matriz. Em
seguida, solicite um número e faça uma busca na matriz por esse número, informando a
posição onde ele se encontra (índice da linha e índice da coluna). Se o número aparecer mais
de uma vez na matriz, exiba todas as posições onde ele foi encontrado.
"""

from random import randint

matriz, vezes, pos, matrizPosicao = [], [], [], []

for i in range(5):
    linha = []
    for j in range(4):
        n = randint(1, 20)
       # n = int(input(f'Posição [{i}, {j}]: '))
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()

num = int(input('Número: '))

for i in range(5):
    pos = []
    for j in range(4):
        if matriz[i][j] == num:
            vezes.append(matriz[i][j])
            pos.append(i)
            pos.append(j)
            matrizPosicao.append(pos)

print(f'O número {num} foi encontrado {len(vezes)} vezes, nas posições {matrizPosicao}')