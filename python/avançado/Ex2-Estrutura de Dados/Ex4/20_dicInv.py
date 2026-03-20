"""Crie um dicionário de inventário (produto -> quantidade). Atualize as
quantidades após uma venda."""

produtos = {"rato" : 5, "teclado" : 2, "mousepad" : 1}
artigo_vendido = input("Introduza o artido vendido: ")
quantidade_vendida = int(input("Digite a quantidade vendida: "))
inventario = produtos.get(artigo_vendido)
atualizado = inventario - quantidade_vendida
produtos[artigo_vendido] = atualizado
for produto, quantidade in produtos.items():
    print(f"{produto} : {quantidade}")