"""Escreva um programa que leia uma matriz 2x2 e calcule a soma de todos os
seus elementos."""

if __name__=="__main__":

    soma = 0
    
    for i in range(2):        
        for j in range(2):
            valor = int(input(f"Digite o elemento [{i}][{j}]: "))
            soma += valor
    print(f"A soma dos elementos da matriz é: {soma}")