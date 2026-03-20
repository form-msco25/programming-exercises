"""Escreva um programa que avalie se uma pessoa é elegível para receber um empréstimo.
O programa deve solicitar a idade, a renda mensal e verificar se a pessoa cumpre os seguintes critérios:
Ser maior de idade
Ter uma renda mensal maior do que 2000€
Se ambos os critérios forem atendidos, exiba "Elegível para o empréstimo".
Caso contrário, exiba "Não elegível para o empréstimo"."""

if __name__ == "__main__":

    idade = int(input("Digite a sua idade: "))
    renda_mensal = int(input("Digite a sua renda mensal em €: "))

    if idade >= 18 and renda_mensal > 2000:
        print("Elegível para o empréstimo")
    else:
        print("Não elegível para o empréstimo")
