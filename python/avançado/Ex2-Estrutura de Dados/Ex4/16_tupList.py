"""Crie um tuplo com 4 cores. Converta-o para uma lista, altere um dos elementos
e depois converta de volta para tuplo."""

tuplo_cores = ("amarillo", "azul", "rojo", "verde")
print(f"Tuplo cores: \n{tuplo_cores}")
lista_cores = list(tuplo_cores)
lista_cores[3] = "blanco"
nova_tuplo_cores = tuple(lista_cores)
print(f"Tuplo cores atualizada: \n{nova_tuplo_cores}")