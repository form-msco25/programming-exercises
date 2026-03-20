"""Converta uma lista com valores repetidos para um set e mostre o set
resultante."""

lista = []
for i in range(5):
    num = int(input("Adicione valores repetidos a uma lista: "))
    lista.append(num)
print(f"A lista criada é: {lista}")
print(f"A lista sem elementos repetidos é: {set(lista)}")