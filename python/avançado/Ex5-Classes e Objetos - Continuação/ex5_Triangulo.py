"""### Descrição
Analise propriedades de triângulos (tipos, área, se é retângulo).
### Atributos
- `lado1`, `lado2`, `lado3` (float): comprimentos dos três lados
### Métodos Obrigatórios
**`__init__(lado1, lado2, lado3)`**
- Inicializa triângulo
- Valida se é um triângulo válido (soma de 2 lados > terceiro lado)
- Se inválido, levanta exceção
**`eh_valido()`**
- Retorna True se é triângulo válido
- Retorna False caso contrário
**`tipo_triangulo()`**
- Retorna string descrevendo o tipo:
- "Equilátero" se os 3 lados são iguais
- "Isósceles" se exatamente 2 lados são iguais
- "Escaleno" se todos os lados são diferentes
**`eh_retangulo()`**
- Verifica se é triângulo retângulo usando Pitágoras
- Retorna True se a2 + b2 = c2
- Retorna False caso contrário
**`calcular_area()`**
- Calcula área usando fórmula de Heron
- Fórmula: s = (a+b+c)/2; area = √(s(s-a)(s-b)(s-c))
- Retorna float"""

import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = float(lado1)
        self.lado2 = float(lado2)
        self.lado3 = float(lado3)
        if not self.eh_valido():
            raise ValueError("Os lados fornecidos não formam um triângulo válido.")
    def eh_valido(self):
        a, b, c = self.lado1, self.lado2, self.lado3
        return (a + b > c) and (a + c > b) and (b + c > a)
    def tipo_triangulo(self):
        a, b, c = self.lado1, self.lado2, self.lado3
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    def eh_retangulo(self):
        # Ordena os lados para garantir que o maior seja o último
        lados = sorted([self.lado1, self.lado2, self.lado3])
        a, b, c = lados
        return math.isclose(a**2 + b**2, c**2)
    def calcular_area(self):
        a, b, c = self.lado1, self.lado2, self.lado3
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
# Teste 1: Triângulo equilátero
tri = Triangulo(5, 5, 5)
print(tri.tipo_triangulo()) # Esperado: "Equilátero"
print(tri.eh_retangulo()) # Esperado: False
# Teste 2: Triângulo isósceles
tri = Triangulo(5, 5, 8)
print(tri.tipo_triangulo()) # Esperado: "Isósceles"
# Teste 3: Triângulo escaleno
tri = Triangulo(3, 4, 5)
print(tri.tipo_triangulo()) # Esperado: "Escaleno"
print(tri.eh_retangulo()) # Esperado: True (32+42=52)
# Teste 4: Cálculo de área (triângulo 3-4-5)
tri = Triangulo(3, 4, 5)
print(tri.calcular_area()) # Esperado: 6.0
# Teste 5: Triângulo inválido
try:
    tri = Triangulo(1, 2, 10) # 1+2 < 10
except:
    print("Triângulo inválido!") # Esperado