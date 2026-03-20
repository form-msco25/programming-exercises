"""Leia uma matriz 3x3 e calcule a soma dos elementos da diagonal principal e da
diagonal secundária."""

import random

matriz = [[random.randint(1,25) for j in range(3)] for i in range(3)]
for linha in matriz:
    print(linha)

soma_principal = 0
soma_secundaria = 0
n = 3
for i in range(n):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][n-1-i]
print(f"A soma da diagonal principal é: {soma_principal}")
print(f"A soma da diagonal secundaria é: {soma_secundaria}")