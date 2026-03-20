"""Peça ao utilizador um nome e verifique, com o operador in, se esse nome está
numa lista predefinida de convidados."""

nomes = ["michael", "carolina", "joana", "tiago", "afonso", "carlos", "jõao"]
nome = input("Coloque o nome do convidado: ").lower()
if nome in nomes:
    print(f"O nome '{nome}' está na lista.")
else:
    print(f"O nome '{nome}' não está na lista.")