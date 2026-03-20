"""Crie um tuplo imutável de coordenadas (x, y, z); faça desempacotamento
em três variáveis e verifique se z é positivo com in num set de valores
válidos."""
coordenadas = (3, 4, -1)
x, y, z = coordenadas
print(f"x = {x}, y = {y}, z = {z}")
valores_validos = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
if z in valores_validos:
    print(f"A variável 'z = {z}' é positivo e está no conjunto de valores válidos.")
else:
    print(f"A variável 'z = {z}' não é positivo ou está no conjunto de valores válidos.")
