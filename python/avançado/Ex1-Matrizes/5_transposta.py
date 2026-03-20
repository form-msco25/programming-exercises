"""Leia uma matriz 2x3 e exiba a sua matriz transposta."""

import random

matriz = [[random.randint(1, 25) for j in range(3)] for i in range(2)]
print(f"Matriz 2x3: ")
for linha in matriz:
    print(linha)
print("=========================")
transposta = [[matriz[i][j] for i in range(2)] for j in range(3)]
print(f"Matriz transposta 3x2: ")
for linha in transposta:
    print(linha)
print("=========================")