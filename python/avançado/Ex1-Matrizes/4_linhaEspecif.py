"""Calcule e exiba a soma dos elementos de uma linha específica de uma matriz
4x4."""

import random

matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = random.randint(1,25)
        linha.append(valor)        
    matriz.append(linha)
print(f"Matriz: ")
for linha in matriz:
    print(linha)
print("=========================")
linha_especifica = int(input("Qual é a linha de elementos que deseja somar? \n"))
soma_linha = sum(matriz[linha_especifica - 1])
print(f"A soma dos elementos da linha {linha_especifica} é: {soma_linha}")