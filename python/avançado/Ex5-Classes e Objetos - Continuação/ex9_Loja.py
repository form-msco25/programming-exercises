"""### Descrição
Gerencia produtos e vendas de uma loja.
### Atributos
- `nome` (string): nome da loja
- `produtos` (dict): {codigo: {'nome': str, 'preco': float, 'estoque': int}}
### Métodos Obrigatórios
**`__init__(nome)`**
- Inicializa loja vazia
**`adicionar_produto(codigo, nome, preco, estoque)`**
- Adiciona novo produto
- Valida se código já existe
- Valida se preço e estoque são positivos
**`remover_produto(codigo)`**
- Remove produto
- Retorna True se removido, False se não existia
**`realizar_venda(codigo, quantidade)`**
- Vende quantidade de um produto
- Valida estoque suficiente
- Reduz estoque
- Retorna valor da venda ou -1 se falhou
**`relatorio_vendas()`**
- Imprime:
- Nome da loja
- Quantidade de produtos
- Valor total em estoque
- Produto mais vendido (fictício ou acompanhar)
**`listar_produtos()`**
- Imprime tabela de produtos:
- Código | Nome | Preço | Estoque"""

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = {}
        self.vendas = {}
    def adicionar_produto(self, codigo, nome, preco, estoque):
        if codigo in self.produtos:
            print(f"Erro: Produto com código {codigo} já existe.")
            return False
        if preco < 0 or estoque < 0:
            print("Erro: Preço e estoque devem ser positivos.")
            return False
        self.produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque}
        self.vendas[codigo] = 0
        return True
    def remover_produto(self, codigo):
        if codigo in self.produtos:
            del self.produtos[codigo]
            del self.vendas[codigo]
            return True
        return False
    def realizar_venda(self, codigo, quantidade):
        if codigo not in self.produtos:
            print("Erro: Produto não encontrado.")
            return -1
        if quantidade <= 0:
            print("Erro: Quantidade inválida.")
            return -1
        if self.produtos[codigo]['estoque'] < quantidade:
            print("Erro: Estoque insuficiente.")
            return -1        
        self.produtos[codigo]['estoque'] -= quantidade
        self.vendas[codigo] += quantidade
        valor_venda = self.produtos[codigo]['preco'] * quantidade
        return valor_venda
    def relatorio_vendas(self):
        print(f"Loja: {self.nome}")
        print(f"Quantidade de produtos: {len(self.produtos)}")
        valor_total_estoque = sum(p['preco'] * p['estoque'] for p in self.produtos.values())
        print(f"Valor total em estoque: R$ {valor_total_estoque:.2f}")
        if self.vendas:
            mais_vendido_codigo = max(self.vendas, key=self.vendas.get)
            mais_vendido = self.produtos[mais_vendido_codigo]['nome']
            print(f"Produto mais vendido: {mais_vendido} (Código: {mais_vendido_codigo})")
        else:
            print("Nenhuma venda registrada.")
    def listar_produtos(self):
        print(f"{'Código':<10} | {'Nome':<20} | {'Preço':<10} | {'Estoque':<10}")
        print("-" * 60)
        for codigo, info in self.produtos.items():
            print(f"{codigo:<10} | {info['nome']:<20} | R$ {info['preco']:<8.2f} | {info['estoque']:<10}")
# Teste 1: Criar loja e adicionar produtos
loja = Loja("Tech Store")
loja.adicionar_produto("P001", "Notebook", 1500.00, 5)
loja.adicionar_produto("P002", "Mouse", 50.00, 20)
loja.adicionar_produto("P003", "Teclado", 150.00, 10)
# Teste 2: Realizar venda
valor = loja.realizar_venda("P001", 2)
print(valor) # Esperado: 3000.0
print(loja.produtos["P001"]["estoque"]) # Esperado: 3
# Teste 3: Venda com estoque insuficiente
valor = loja.realizar_venda("P002", 25)
print(valor) # Esperado: -1 (falha)
# Teste 4: Listar produtos
loja.listar_produtos()
# Teste 5: Relatório
loja.relatorio_vendas()
# Teste 6: Remover produto
loja.remover_produto("P003")
print(len(loja.produtos)) # Esperado: 2