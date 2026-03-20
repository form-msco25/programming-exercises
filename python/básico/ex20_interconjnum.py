"""Cria um programa que:
Leia dois conjuntos de números introduzidos pelo utilizador (cada conjunto com 5 números).
Construa os dois sets a partir dos números fornecidos.

Determine:
A interseção (números em comum).
A diferença (números que existem apenas no primeiro).

Se a interseção estiver vazia, mostre a mensagem "Não há números em comum.",
senão mostre os números partilhados."""

if __name__ == "__main__":

    conj_num1 = set()
    conj_num2 = set()

    while len(conj_num1) < 5:
        i = input("Digite um número inteiro para o conjunto número 1: ")
        conj_num1.add(int(i)) if i.isdigit() else print("Por favor insira números inteiros.")        
    print(conj_num1)

    while len(conj_num2) < 5:
        i = input("Digite um número inteiro para o conjunto número 2: ")
        conj_num2.add(int(i)) if i.isdigit() else print("Por favor insira números inteiros.")   
    print(conj_num2)

    intersecao_conj = conj_num1 & conj_num2
    if len(intersecao_conj) != 0:
        print(f"Os números inteiros em comum são: {intersecao_conj}")
    else:
        print("Não há elementos em comum.")

    diferenca_conj1 = conj_num1 - conj_num2
    if len(diferenca_conj1) != 0:
        print(f"Os números que só existem no primeiro conjunto são: {diferenca_conj1}")
    else:
        print("Não existem números únicos no primeiro conjunto.")