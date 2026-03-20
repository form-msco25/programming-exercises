"""O programa que vamos criar irá simular o controle de estoque de uma pequena loja de eletrônicos.

A primeira coisa que precisamos é da estrutura de dados. O seu programa deve começar com o dicionário em anexo, que representa o nosso estoque.

Observe que temos dicionários aninhados (categorias como "smartphones", "laptops", etc.), e dentro deles, uma lista de dicionários chamada "modelos", 
onde cada dicionário representa um produto com seu nome, preço e quantidade.

O seu trabalho é escrever um programa que, usando essa estrutura, realize as seguintes operações:

Exibir o Estoque Total: Percorra o dicionário e imprima o nome e a quantidade de cada produto em estoque.
Buscar um Produto: Implemente a funcionalidade de pesquisar o dicionário completo desse produto (com nome, preço e quantidade). 
Se o produto não for encontrado, Mostre uma mensagem de erro.
Atualizar a Quantidade: Crie a funcionalidade para atualizar o nome de um produto e a quantidade a ser adicionada 
(pode ser um valor negativo para remover). Deve encontrar o produto e atualizar a sua quantidade. 
Por exemplo, se vender 5 unidades de um produto, ela deve subtrair 5 da quantidade atual. Não pode ficar com stock negativo!

Crie um menu adequado para utilizar estas funcionalidades com as mensagens adequadas."""

def mostrar_stock():
    print("\nINVENTÁRIO\n")
    for categoria, info in estoque_eletronicos.items():
        marca = info["marca"]
        print(f"\nCategoria: {categoria.capitalize()}\nMarca: {marca}")        
        for produto in info["modelos"]:
            nome = produto["nome"]
            quantidade = produto["quantidade"]
            print(f"Produto: {nome} | Quantidade: {quantidade}")

def procurar_produto(nome_procura):
    for info in estoque_eletronicos.values():
        for produto in info["modelos"]:
            if produto["nome"].lower() == nome_procura.lower():
                return produto
    return None
    
def atualizar_quantidade(nome, quantidade):
    produto = procurar_produto(nome)
    if produto is None:
        print("Produto não encontrado.")
        return #encerra a função se esta condição for verdadeira     
    nova_quantidade = produto["quantidade"] + quantidade
    if nova_quantidade < 0:
        print("Operação inválida: inventário não pode ficar negativo.")
    else:
        produto["quantidade"] = nova_quantidade
        print(f"Quantidade atualizada! Novo inventário: {produto['quantidade']}")

if __name__ == "__main__":
    estoque_eletronicos = {
        "smartphones": {
            "marca": "Apple",
            "modelos": [
                {"nome": "iPhone 14 Pro", "preco": 1200, "quantidade": 25},
                {"nome": "iPhone 14", "preco": 800, "quantidade": 50},
                {"nome": "iPhone SE", "preco": 450, "quantidade": 15}
            ]
        },
        "laptops": {
            "marca": "Dell",
            "modelos": [
                {"nome": "XPS 15", "preco": 2000, "quantidade": 10},
                {"nome": "Inspiron 14", "preco": 750, "quantidade": 30}
            ]
        },
        "acessorios": {
            "marca": "Diversas",
            "modelos": [
                {"nome": "Fone de Ouvido sem Fio", "preco": 150, "quantidade": 100},
                {"nome": "Capa para Smartphone", "preco": 25, "quantidade": 200},
                {"nome": "Carregador USB-C", "preco": 30, "quantidade": 150}
            ]
        }
    }
    cond = True
    while cond:
        print("\n===== MENU =====")
        print("1 - Mostrar inventário")
        print("2 - Procurar produto")
        print("3 - Atualizar quantidade")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_stock()

        elif opcao == "2":
            nome = input("Digite o nome do produto: ")
            produto = procurar_produto(nome)

            if produto:
                print("\nPRODUTO ENCONTRADO")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: {produto['preco']}")
                print(f"Quantidade: {produto['quantidade']}")
            else:
                print("Produto não encontrado.")

        elif opcao == "3":
            nome = input("Digite o nome do produto: ")
            try:
                quantidade = int(input("Digite a quantidade a adicionar/remover: "))
                atualizar_quantidade(nome, quantidade)
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "4":
            print("Encerrando o programa...")
            cond = False

        else:
            print("Opção inválida!")