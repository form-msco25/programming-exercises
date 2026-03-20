"""Leia uma matriz 3x3 e determine qual linha ou coluna tem a maior soma."""

import random

linha = 3
coluna = 3

matriz = [[random.randint(1,25) for j in range(coluna)] for i in range(linha)]
print("Matriz: " )
for linha in matriz:
    print(linha)

somas_linhas = [sum(linha) for linha in matriz]

indice_linha = somas_linhas.index(max(somas_linhas))
linha_maior_soma = matriz[indice_linha]
print("Linha com maior soma:", linha_maior_soma)
print("Soma:", max(somas_linhas))

num_colunas = len(matriz[0])

somas_colunas = []
for j in range(num_colunas):
    soma = sum(matriz[i][j] for i in range(len(matriz)))
    somas_colunas.append(soma)

indice_coluna = somas_colunas.index(max(somas_colunas))
coluna_maior_soma = [linha[indice_coluna] for linha in matriz]
print("Coluna com maior soma:", coluna_maior_soma)
print("Soma:", max(somas_colunas))