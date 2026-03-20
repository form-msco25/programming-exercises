"""Faça um programa, que leia dois números e a seguir imprima a sua soma,
subtração, multiplicação e divisão."""

if __name__ == "__main__":
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número inteiro: "))

    print(f"A soma dos número é igual a {num1+num2}.\n")
    print(f"A subtração dos número é igual a {num1-num2}.\n")
    print(f"A multiplicação dos número é igual a {num1*num2}.\n")
    print(f"A divisão dos número é igual a {num1/num2}.\n")