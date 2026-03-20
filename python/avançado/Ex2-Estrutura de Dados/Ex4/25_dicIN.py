"""Usando um dicionário que guarda o stock de uma loja, verifique com in se um
produto pedido pelo cliente existe antes de tentar aceder ao seu valor."""

stock = {"pc":799, "portatil":599, "ps5":499, "rato":59, "teclado":49}
produto = input("Introduza o produto que deseja procurar: ").lower()
if produto in stock:
    print(f"O produto '{produto}' está disponível.\nO seu valor é: {stock.get(produto)}")
else:
    print(f"O produto '{produto}' não está disponível.")