"""Crie uma classe `Estudante` com os seguintes atributos:
- `nome` (string)
- `matricula` (string)
- `notas` (lista de números)
Implemente os seguintes métodos:
- `adicionar_nota(nota)`: adiciona uma nota à lista de notas
- `calcular_media()`: retorna a média aritmética das notas
- `verificar_aprovacao()`: retorna True se a média ≥ 10, False caso contrário
- `exibir_status()`: imprime nome, matrícula, média e status de aprovação
**Teste:** Crie um estudante, adicione 4 notas (12, 14, 9, 11) e exiba o status."""

class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.lista_notas = []
    def adicionar_nota(self, nota):
        self.lista_notas.append(float(nota))
    def calcular_media(self):
        return sum(self.lista_notas)/len(self.lista_notas)
    def verificar_aprovacao(self):
        return self.calcular_media() >= 10
    def exibir_status(self):
        media = self.calcular_media()
        status = "Aprovado" if self.verificar_aprovacao() else "Reprovado"
        print(f"Nome: {self.nome}\nMatrícula: {self.matricula}\nMédia: {media:.2f}\nStatus: {status}")
est = Estudante("Michael", 12345)

est.adicionar_nota(12)
est.adicionar_nota(14)
est.adicionar_nota(9)
est.adicionar_nota(11)

est.exibir_status()