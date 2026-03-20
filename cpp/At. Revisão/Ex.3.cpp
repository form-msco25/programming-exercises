#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

// Escreva um programa em C para ler n números inteiros para um vetor e mostre o maior elemento desse vetor. 
// Nota: Utilize uma função que retorne o maior elemento..

int maior_elem(int vetor[], int n) {
    int maior = vetor[0];
    
    for (int i = 0; i < n; i++) {
        if (vetor[i] > maior)
            maior = vetor[i];
    }
    return maior;
}

int main() {
	
	setlocale (LC_ALL, "Portuguese");
	
    int n;

    printf("Digite a quantidade de números: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("O tamanho do vetor deve ser maior que zero.\n");
        return 1;
    }

    int vetor[n];
    
    printf("Digite %d números inteiros:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%d", &vetor[i]);
    }

    int maior = maior_elem(vetor, n);

    printf("\nO maior elemento do vetor é: %d\n", maior);

    return 0;
}