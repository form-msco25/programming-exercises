"""Dado um set de frutas duplicadas de uma lista de compras, remova
duplicados, adicione uma nova fruta com add() e verifique com in se
"maçã" existe."""
lista_frutas_A = ["banana", "maçã", "laranja", "tomate", "limão", "pêssego", "manga"]
lista_frutas_B = ["ananâs", "melancia", "banana", "manga", "maracujá", "tangerina", "pera"]
set_frutas = set((lista_frutas_A + lista_frutas_B))
print(f"Set de frutas sem duplicadas: {set_frutas}")
nova_fruta = "kiwi"
set_frutas.add(nova_fruta)
print(f"Set de frutas atualizado: {set_frutas}")