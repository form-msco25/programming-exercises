"""Utilizando a instrução SET faça as seguintes operações:
a. Adicione 5 países
b. Liste os países
c. Remova um país a sua escolha
d. Insira um país já existente
e. Imprima os países e o número de países existentes"""

paises = set()
for i in range(5):
    pais = input("Introduza um país: ").lower()
    paises.add(pais)
print(f"Países inseridos: {paises}")
remover = input("Digite o país que deseja eliminar: ").lower()
paises.discard(remover)
repetido = input(f"Dos seguintes países: {paises}\nColoque o que pretende duplicar: ").lower()
paises.add(repetido)
print(f"Países: {paises}\nNúmero de países: {len(paises)}")