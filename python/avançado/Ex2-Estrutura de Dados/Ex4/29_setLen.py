"""Usando um set, remova todos os valores repetidos de uma lista de inscrições
numa formação e apresente quantos participantes únicos existem."""

lista_inscricoes = [1, 2, 2, 3, 4, 4, 5]
print(f"Lista original de inscrições é: {lista_inscricoes}.\nLista sem inscrições repetidas é: {set(lista_inscricoes)}.")
print(f"Número definitivo de inscrições é: {len(set(lista_inscricoes))}")