"""Escreva um programa que receba o peso (em quilogramas) de uma pessoa. Com base no peso, determine e exiba a categoria de peso da pessoa:
"Peso leve"  até 70.3Kg
"Peso médio" de 70.3 até 83.95kg
"Peso pesado" de 83.95 para cima"""

if __name__ == "__main__":

    peso = float(input("Digite o seu peso em kg: "))

    if peso < 70.3:
        print("Peso leve")
    elif peso >= 70.3 and peso < 83.95:
        print("Peso médio")
    else:
        print("Peso pesado")