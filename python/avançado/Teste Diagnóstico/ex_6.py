"""Crie uma função chamada "calculaArea" que receba o raio de um círculo como
parâmetro e retorne a área desse círculo (área= PI*raio^2). Utilize a constante
PI(3.14f) para calcular a área."""

import math
if __name__=="__main__":
    raio = float(input("Digite o raio de um cículo: "))
    area = math.pi*(raio**2)
    print("O raio do círculo é %.2f" % area)