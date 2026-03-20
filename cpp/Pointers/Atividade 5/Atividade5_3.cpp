#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
/* Escreva um programa para calcular o comprimento de uma string usando apenas
apontadores (utilize uma função que retorne o tamanho); */
int comprimento(const char *str){
    const char *p = str;
    while (*p != '\0') {
        p++;        
	}
	return p - str;
}
int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    char texto[100];

    printf("Digite uma string: ");
    fgets(texto, 100, stdin);
    
    char *p = texto;
    while (*p != '\0') {
        if (*p == '\n') {
            *p = '\0';
            break;
        }
        p++;
    }
    
    printf("Comprimento: %d\n", comprimento(texto));
    
    return 0;
}