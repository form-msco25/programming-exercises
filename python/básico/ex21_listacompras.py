"""Desenvolve um programa que:
Tenha inicialmente um set com os produtos: "pão", "leite", "arroz", "maçã".
Permita ao utilizador adicionar produtos através de um ciclo while, terminando quando este escrever "sair".
Se o produto já estiver no conjunto, mostra "Produto já existe na lista!".
Caso contrário, adiciona-o e mostra "Produto adicionado.".
No final, imprime a lista de produtos organizada por ordem crescente do nome."""

if __name__ == "__main__":
    set_lista_compras = {"pão", "leite", "arroz", "maçã"}
    adicionar = input(f"A sua lista de compras é: \n{set_lista_compras}. Digite S / N se desejar adicionar novos produtos.\n").lower()
    if adicionar == "s":
        cond = True
    else:
        cond = False
        print("Até breve!")
    
    while cond:
        produto = input("Digite 'sair' para finalizar o programa.\nIntroduza um novo item: ").lower()
        if produto == "sair":
            cond = False
        elif produto.isalpha() == False:
            print("Só pode introduzir produtos.")
            cond = False
        elif produto in set_lista_compras:
            print(f"Produto já existente: {produto}")
        else:
            set_lista_compras.add(produto)
            print(f"Produto adicionado: {produto}")            
        print(f"Lista de compras é a seguinte:\n{set_lista_compras}")
    lista_compras = sorted(set_lista_compras)
    print("Lista de compras por ordem alfabética:\n", lista_compras)
        