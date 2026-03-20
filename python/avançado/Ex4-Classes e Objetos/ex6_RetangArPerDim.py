"""Crie uma classe `Retangulo` com os seguintes atributos:
- `largura` (float)
- `altura` (float)
Implemente os seguintes métodos:
- `calcular_area()`: retorna largura × altura
- `calcular_perimetro()`: retorna 2 × (largura + altura)
- `exibir_dimensoes()`: imprime largura, altura, área e perímetro
**Teste:** Crie um retângulo com largura 10 e altura 5, depois exiba as dimensões."""

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = float(largura)
        self.altura = float(altura)
    def calcular_area(self):
        return self.largura * self.altura
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    def exibir_dimensoes(self):
       print(f"Largura: {self.largura}\nAltura: {self.altura}")
       print(f"Área: {self.calcular_area()}\nPerímetro: {self.calcular_perimetro():.2f}")

retangulo = Retangulo(10, 5)
retangulo.exibir_dimensoes()