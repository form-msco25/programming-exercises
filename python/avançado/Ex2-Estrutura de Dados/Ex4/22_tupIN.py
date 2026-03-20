"""Crie um tuplo com 3 cidades e utilize o operador in para verificar se 'Braga' faz
parte do tuplo."""

lista_cidades = []
for i in range(3):
    cidade = input("Digite uma cidade: ").lower()
    lista_cidades.append(cidade)
tuplo_cidades = tuple(lista_cidades)
verificar = "braga"
if verificar in tuplo_cidades:
    print(f"A cidade {verificar} está no conjunto de cidades.")
else:
    print(f"A cidade {verificar} não está no conjunto de cidades.")