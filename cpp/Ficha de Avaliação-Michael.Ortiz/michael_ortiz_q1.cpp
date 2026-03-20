#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <ctype.h>

/* Crie um programa que aceite 3 valores de vendas inseridos pelo utilizador e
apresente a sua média com 1 casa decimal. Imprima igualmente as situações
“Objetivo ultrapassado”, se média das vendas > 100, “Objetivo atingido”, se a
média das vendas for 100 e “Objetivo não atingido” se média < 100. */

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    float val1, val2, val3, media;
    
    printf("Insira 3 valores de vendas: \n");
    scanf("%f %f %f", &val1, &val2, &val3);
    
    media = ((val1 + val2 + val3))/3;
    
    printf("A média dos 3 valores é: %1.f \n", media);
    
    if ( media> 100){
    	printf("Objetivo ultrapassado.\n");
	}
    	
    else if ( media == 100){
    		printf("Objetivo atingido.\n");
	}
	
	else {
		printf("Objetivo não atingido.\n");
	}
    
    return 0;
}