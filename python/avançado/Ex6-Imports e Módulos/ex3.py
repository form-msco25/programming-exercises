import random

numero_aleatorio = random.randint(1, 100)

cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
cor_aleatoria = random.choice(cores)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numeros)

print(f"Número aleatório entre 1 e 100: {numero_aleatorio}")
print(f"Cor aleatória escolhida: {cor_aleatoria}")
print(f"Lista de números embaralhada: {numeros}")