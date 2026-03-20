"""Escreva um programa que leia 10 números inteiros do utilizador e os armazene
num array. Em seguida, verifique se um número específico fornecido pelo
utilizador está presente no array. Se estiver, imprima "O número está presente
no array". Se não estiver, imprima "O número não está presente no array"."""

if __name__=="__main__":
    
    lista_num = []
    for i in range(10):
        num = int(input("Digite um número inteiro: "))         
        if num in lista_num:
            print("O número está presente no array.")
        else:
            print("O número não está presente no array.")
            lista_num.append(num)
        print(lista_num)