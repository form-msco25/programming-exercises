#include <stdio.h>
#include <locale.h>

/* Escreva um programa em C para demonstrar como lidar com ponteiros num programa.:
A saída esperada para o programa é:
Endereço de m: ENDEREÇO m
Valor de m: 29
Agora ab é atribuído com o endereço de m.
Endereço do ponteiro ab: ENDEREÇO ab
Conteúdo apontado por ab: 29
Agora o valor atribuído a m é 34
Endereço do ponteiro ab: ENDEREÇO ab
Conteúdo apontado por ab: 34
A variável apontada por ab agora recebe o valor 7.
Endereço de m: ENDEREÇO m
Valor de m: 7 */

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int m = 29;
	printf("Valor de m: %d \n", m);
	int *ab;
	ab = &m;
    printf("Endereço de m: %x \n", &m);    
    printf("Endereço do ponteiro ab: %x \n", &ab);    
    printf("\nConteúdo de ab : %d \n", *ab);
    
    m = 34;
    printf("Valor de m: %d \n", m);
    printf("Endereço do ponteiro ab: %x \n", &ab);
    printf("\nConteúdo de ab : %d \n", *ab);
    
    *ab = 7;
    printf("Endereço de m: %x \n", &m);
    printf("Valor de m: %d \n", m);
    
    return 0;
}