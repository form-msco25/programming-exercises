"""Crie uma classe `Produto` com os seguintes atributos:
- `nome` (string)
- `preco` (float)
- `quantidade_estoque` (inteiro)
Implemente os seguintes métodos:
- `adicionar_estoque(quantidade)`: aumenta o estoque
- `remover_estoque(quantidade)`: diminui o estoque (verifica se há quantidade
suficiente)
- `calcular_valor_total()`: retorna preco × quantidade_estoque
- `exibir_info()`: imprime as informações do produto com saldo total
**Teste:** Crie um produto, adicione 50 unidades, remova 15, adicione 20
novamente e exiba as informações. """
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = 0
    def adicionar_stock(self, quantidade):
        self.quantidade += quantidade
    def remover_stock(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print("Produto esgotado")
    def calcular_valor_total(self):
        return self.preco * self.quantidade
    def exibir_info(self):
        print(f"Nome do produto: {self.nome}\nPreço: {self.preco:.2f}\nQuantidade: {self.quantidade}\nValor total: {self.calcular_valor_total():.2f}")
prod = Produto("PC", 999)
prod.adicionar_stock(50)
prod.remover_stock(15)
prod.adicionar_stock(20)
prod.exibir_info()