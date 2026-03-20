"""A partir de um dicionário de preços de produtos, peça ao utilizador o nome de
um produto e mostre o preço correspondente."""

loja = {"portátil" : 999, "pc" : 1199, "ps4" : 499}
produto = input("Introduza o produto: ").lower()
print(f"O preço do produto selecionado é {loja[produto]}")
