"""Crie um dicionário onde as chaves são números e os valores são os quadrados
desses números (por exemplo, 2:4, 3:9) para os números de 1 a 5."""

dicionario = {}
for i in range(5):
    num = int(input("Digite um número: "))
    quad = num**2
    dicionario[num] = quad
print(dicionario)
