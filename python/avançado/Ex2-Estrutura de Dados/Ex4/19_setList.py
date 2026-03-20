"""Use um set para descobrir quais números, entre 1 e 20, aparecem numa lista
de resultados de testes (com repetições)."""

from random import randint

lista_num = [randint(1, 20) for i in range(20)]
print(f"Lista de resultados: {lista_num}")
set_num = set(lista_num)
print(f"Resultados sem repetições: {set_num}")
repetidos = {num for num in set_num if lista_num.count(num) > 1}
print(f"Números repetidos: {repetidos}")