#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
/* Escreva um programa para guardar n elementos num vetor, passe esse vetor a uma
função, multiplicando todos os elementos do vetor por 2. Imprima o vetor na função e
o vetor antes e depois da chamada à função.*/

int multiplicar(int v[], int i){
	int resultado = 0;
	
	for (int i=0; i<n; i++){
		resultado = v[i]*2;
	} 
	return resultado;
}

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int n;
    printf("Digite a quantidade de números: ");
    scanf("%d", &n);

    if (n<=0){
        printf("O tamanho do vetor deve ser maior que zero.\n");
        return 1;
    }
    
    int v[n];
    int i;
    printf("Digite %d números inteiros:\n", n);
    for (i=0; i<n; i++){
        printf("Elemento %d: ", i+1);
        scanf("%d", &v[i]);
    }
    int resultado = multiplicar(v, i);
    for (int i=0; i<n; i++){
        printf("Elemento %d: %d\n", i+1, v[i]);           
    }
	    
    return 0;
}
