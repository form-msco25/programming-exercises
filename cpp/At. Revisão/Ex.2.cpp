#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

// Escreva um programa em C para verificar se dois inteiros não negativos, têm o mesmo último dígito. 
// Nota 1: utilize uma função para verificar essa situação. Nota 2: para confirmar a não negatividade, utilize a função matemática "abs()".
// Dica: utilize o resto da divisão inteira para comparar o último dígito de cada um dos números.

int ult_dig(int a, int b) {
    
    a = abs(a);
    b = abs(b);

    if ((a % 10) == (b % 10))
        return 1;
    else
        return 0;
}

int main() {
	
	setlocale (LC_ALL, "Portuguese");
    
    int num1, num2;

    printf("Digite o primeiro número inteiro: ");
    scanf("%d", &num1);

    printf("Digite o segundo número inteiro: ");
    scanf("%d", &num2);

    if (num1 < 0 || num2 < 0) {
        printf("Digite apenas números não negativos.\n");
        return 1;
    }

    if (ult_dig(num1, num2))
        printf("Os números %d e %d têm o mesmo último dígito.\n", num1, num2);
    else
        printf("Os números %d e %d NÃO têm o mesmo último dígito.\n", num1, num2);

    return 0;
}