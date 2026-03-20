#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
/* Escreva um programa que receba um vetor de inteiros de 10 elementos e indique,
através de uma função, o maior elemento desse vetor (Nota: utiliza passagem por
referência).*/

int maior_elem(int v[], int n){
	int maior = v[0];
	
	for (int i=0; i<n; i++){
		if (v[i]>maior)
		maior = v[i];
	}
	return maior;
}

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int n=10;   
    int v[n];
    
    for (int i=0; i<n; i++){
    	printf("Digite %d números inteiros:", n);
    	scanf("%d", &v[i]);
	}
	
	int maior = maior_elem(v, n);
	int *p;
	p = &maior;
	printf("\nO maior elemento do vetor é: %d\n", *p);
    
    return 0;
}