#include <stdio.h>
#include <locale.h>

/* 1 - Escreva um programa em C para mostrar a declaração básica de um ponteiro
Condição prévia: m = 10, n e o são duas variáveis inteiras e *z é um inteiro
Saída esperada do programa:
z armazena o endereço de m = ENDEREÇO m
*z armazena o valor de m = 10
&m é o endereço de m = ENDEREÇO
&n armazena o endereço de n = ENDEREÇO n
&o armazena o endereço de o = ENDEREÇO o
&z armazena o endereço de z = ENDEREÇO z */

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int n=1;
	int o=2; 
	int *z;
    int m=10;
    z = &m;
    
    printf("z armazena o endereço de m = %p \n", z);
    printf("*z armazena o valor de m = %d \n", *z);
    printf("&m é o endereço de m = %p \n", &m);
	printf("&n armazena o endereço de n = %p \n", &n);
	printf("&o armazena o endereço de o = %p \n", &o);
	printf("&z armazena o endereço de z = %p \n", &z);    
    
    return 0;
}