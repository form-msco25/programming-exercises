"""Construa uma matriz 3 por 3 e realize as seguintes operações:
a. Leia valores para a matriz
b. Devolva a media de todos os valores lidos.
c. Devolva quantos número positivo, negativos e nulos.
d. Devolva quantos pares e ímpares.
e. E por fim multiplique cada um dos elementos lidos por 10 e a seguir
imprima."""

import random

matriz_A = [[random.randint(-10,10) for j in range(3)] for i in range(3)]
print("Matriz A: " )
for linha in matriz_A:
    print(linha)

matriz_B = [[random.randint(-10,10) for j in range(3)] for i in range(3)]
print("Matriz B: " )
for linha in matriz_B:
    print(linha)

soma = [[matriz_A[i][j] + matriz_B[i][j] for j in range(3)] for i in range(3)]
media = [[soma[i][j] // 2 for j in range(3)] for i in range(3)]
print("Média das matrizes A e B: ")
for linha in media:
    print(linha)
print("===================================")
pos_A = 0
neg_A = 0
nul_A = 0
for i in range(3):
    for j in range(3):
        if matriz_A[i][j] > 0:
            pos_A += 1
        elif matriz_A[i][j] < 0 :
            neg_A += 1
        else:
            nul_A += 0
print("Matriz A: ")
print(f"Quantidade de números positivos: {pos_A}")
print(f"Quantidade de números negativos: {neg_A}")
print(f"Quantidade de números nulos: {nul_A}")
print("===================================")
pos_B = 0
neg_B = 0
nul_B = 0
for i in range(3):
    for j in range(3):
        if matriz_B[i][j] > 0:
            pos_B += 1
        elif matriz_B[i][j] < 0 :
            neg_B += 1
        else:
            nul_B += 0
print("Matriz B: ")
print(f"Quantidade de números positivos: {pos_B}")
print(f"Quantidade de números negativos: {neg_B}")
print(f"Quantidade de números nulos: {nul_B}")
print("===================================")
par_A = 0
impar_A = 0
for i in range(3):
    for j in range(3):
        if matriz_A[i][j]==0:
            continue
        elif matriz_A[i][j]%2==0:
            par_A += 1
        else:
            impar_A += 1
print("Matriz A: ")
print(f"Quantidade de números pares: {par_A}")
print(f"Quantidade de números ímpares: {impar_A}")
print("===================================")
par_B = 0
impar_B = 0
for i in range(3):
    for j in range(3):
        if matriz_B[i][j]==0:
            continue
        elif matriz_B[i][j]%2==0:
            par_B += 1
        else:
            impar_B += 1
print("Matriz B: ")
print(f"Quantidade de números pares: {par_B}")
print(f"Quantidade de números ímpares: {impar_B}")
print("===================================")
mult_A = [[matriz_A[i][j]*10 for j in range(3)] for i in range(3)]
print("Matriz A multiplicada por 10: ")
for linha in mult_A:
    print(linha)
print("===================================")
mult_B = [[matriz_B[i][j]*10 for j in range(3)] for i in range(3)]
print("Matriz A multiplicada por 10: ")
for linha in mult_B:
    print(linha)
print("===================================")