"""Crie uma classe `Funcionario` com os seguintes atributos:
- `nome` (string)
- `salario` (float)
- `departamento` (string)
Implemente os seguintes métodos:
- `aumentar_salario(percentual)`: aumenta o salário em um percentual
- `calcular_inss()`: calcula e retorna 11% do salário
- `calcular_salario_liquido()`: retorna salário - INSS
- `exibir_info()`: imprime nome, departamento, salário bruto, INSS e salário líquido
**Teste:** Crie um funcionário com salário de 3000, aumente em 10% e exiba as
informações."""

class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento
    def aumentar_salario(self, percentual):       
        self.salario += self.salario * (percentual / 100)
    def calcular_inss(self):
        return self.salario * 0.11
    def calcular_salario_liquido(self):
        return self.salario - self.calcular_inss()
    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Departamento: {self.departamento}")
        print(f"Salário bruto: {self.salario}")
        print(f"INSS: {self.calcular_inss()}")
        print(f"Salário líquido: {self.calcular_salario_liquido()}")
fun1 = Funcionario("Michael", 3000, "Informática")
fun1.aumentar_salario(10)
fun1.calcular_inss()
fun1.calcular_salario_liquido()
fun1.exibir_info()