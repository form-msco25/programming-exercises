"""Crie uma lista de números inteiros e utilize o operador in para verificar se o
número 7 está presente."""

lista = []
n = int(input("Quantos elementos pretende inserir na lista?\n"))
for i in range(n):
    elemento = int(input("Insira números inteiros à lista: "))
    lista.append(elemento)
resposta = input("Deseja verificar se existe um número na lista? Digite s/n: ").lower()
while resposta=="s":
    num = input("Digite o inteiro que pretende verificar: ")
    if num.isdigit():
        num = int(num)
        if num in lista:
            print(f"O número {num} encontra-se na lista.")
            saida = input("Para finalizar o programa digite 'sair' ou 'seguir' para continuar.\n").lower()
            if saida == "sair":
                resposta = "n"
        else:
            print(f"O número {num} não se encontra na lista.")
            saida = input("Para finalizar o programa digite 'sair' ou 'seguir' para continuar.\n").lower()
            if saida == "sair":
                resposta = "n"
    else:
        print("Entrada inválida. Digite um número inteiro.")
print("Fim do programa.")