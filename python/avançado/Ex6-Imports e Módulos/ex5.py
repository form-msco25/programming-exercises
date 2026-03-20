import math, random
from datetime import datetime

numero_aleatorio = random.randint(1, 10)

raiz_quadrada = math.sqrt(numero_aleatorio)

data_hora_atual = datetime.now()

print(f"Número aleatório entre 1 e 10: {numero_aleatorio}")
print(f"Raiz quadrada do número: {raiz_quadrada}")
print(f"Data e hora atual: {data_hora_atual}")