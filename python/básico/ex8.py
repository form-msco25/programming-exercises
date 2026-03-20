""" Crie um programa em Python que utilize o módulo random para gerar um número inteiro aleatório entre 1 e 10.

O usuário deve digitar um número tentando adivinhar o valor sorteado.

Se o usuário acertar o número, o programa deve exibir uma mensagem de parabéns.

Se o usuário errar, o programa deve informar se o número secreto é maior ou menor do que o palpite digitado.

Ao final, o programa deve mostrar qual era o número secreto."""

from random import randint

if __name__ == "__main__":

    r = randint(1,10)
    n = int(input("Digite um número inteiro e tente adivinhar o número secreto: "))

    if r==n:
        print("Parabéns!")
    elif r>n:
            print("O número secreto é maior")
    else:
        print("O número secreto é menor")

    print(f"O número secreto é {r}")