"""Faça um programa que crie uma lista com 5 tipos de frutas e a seguir execute
as seguintes tarefas:
a. Liste a lista
b. Insira uma nova fruta
c. Liste a lista
d. Ordene a lista
e. Liste a lista
f. Elimine um elemento da lista
g. Liste a lista
h. Mostre somente o 2o elemento da lista
i. Imprima caracter a caracter a terceira fruta da lista"""

frutas = ["banana", "laranja", "limão", "pêssego", "maçã"]
print(f"Lista de frutas: {frutas}")
nova_fruta = "morango"
frutas.append(nova_fruta)
print(f"Lista de frutas atualizada: {frutas}")
frutas.sort()
print(f"Lista de frutas ordenada: {frutas}")
fruta_eliminada = frutas.pop()
print(f"Fruta eliminada: {fruta_eliminada}")
print(f"Lista atualizada novamente: {frutas}")
print(f"Segundo elemento da lista: {frutas[1]}")
caracter = list(frutas[2])
print(f"A terceira fruta separada por caracteres: {caracter}")