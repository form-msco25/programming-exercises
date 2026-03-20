"""Crie duas matrizes 2x2 preenchidas pelo utilizador e calcule a matriz resultante
da sua multiplicação."""

matriz_A = [[int(input(f"Para a Matriz A digite o elemento[{i}][{j}]: ")) for j in range(2)] for i in range(2)]
print("Matriz A: ")
for linha in matriz_A:
    print(linha)
print("=========================")
matriz_B = [[int(input(f"Para a Matriz B digite o elemento[{i}][{j}]: ")) for j in range(2)] for i in range(2)]
print("Matriz B: ")
for linha in matriz_B:
    print(linha)
print("=========================")
mult = [[0 for j in range(2)] for i in range(2)]
for i in range(2):
    for j in range(2):
        for k in range(2):
            mult[i][j] += matriz_A[i][k] * matriz_B[k][j]
print("Matrizes multiplicadas: ")
for linha in mult:
    print(linha)