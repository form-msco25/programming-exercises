"""Leia uma matriz 3x3 e determine o maior elemento presente nela."""

import random

linha = 3
coluna = 3

matriz = [[random.randint(1,25) for j in range(coluna)] for i in range(linha)]
print("Matriz: " )
for linha in matriz:
    print(linha)

maior = matriz[0][0]
linha_maior = coluna_maior = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"Maior elemento da matriz: {maior}")
print(f"Posição:  Matriz[{linha_maior}][{coluna_maior}]")