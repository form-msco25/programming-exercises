"""Com um dicionário de stock (produto: quantidade), peça input do
utilizador, verifique com in se existe e subtraia 1 da quantidade se
disponível."""
inventario = {"melancia": 5, "banana": 3, "laranja": 4, "pera": 2}
produto = input("Introduza o nome do produto: ").lower()
if produto in inventario:
    if inventario[produto] > 0:
        inventario[produto] -= 1
        print(f"Produto vendido. Stock atual de {produto}: {inventario[produto]}")
    else:
        print(f"O produto '{produto}' não tem stock disponível.")
else:
    print("Produto não encontrado no inventário.")
print("Inventário atualizado:", inventario)
