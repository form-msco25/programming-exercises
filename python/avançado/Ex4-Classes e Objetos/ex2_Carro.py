"""Crie uma classe `Carro` com os seguintes atributos:
- `marca` (string)
- `modelo` (string)
- `ano` (inteiro)
- `velocidade_atual` (inteiro, começando em 0)
Implemente os seguintes métodos:
- `acelerar(valor)`: aumenta a velocidade_atual em `valor` unidades
- `travar(valor)`: diminui a velocidade_atual em `valor` unidades (não pode ser
negativa)
- `mostrar_velocidade()`: imprime a velocidade atual do carro
**Teste:** Crie um carro, acelere 3 vezes (+20, +15, +10) e trabe uma vez (-30)."""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = 0
    def acelerar(self, valor):        
        self.velocidade_atual += valor
    def travar(self, valor):
        self.velocidade_atual -= valor
        if self.velocidade_atual < 0:
            self.velocidade_atual = 0
    def mostrar_velocidade(self):
        print(f"Velocidade atual: {self.velocidade_atual}")
carro = Carro("Honda", "Civic", 2012)
carro.acelerar(20)
carro.acelerar(15)
carro.acelerar(10)
carro.travar(30)
carro.mostrar_velocidade()