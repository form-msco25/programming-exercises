"""Faça um programa que leia 3 números e diga qual é o maior e o menor."""
if __name__ == "__main__":
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número inteiro: "))
    num3 = int(input("Digite um número inteiro: "))

    lista_num = [num1, num2, num3]
    print(f"O número maior é: {max(lista_num)}")