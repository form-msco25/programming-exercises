#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <ctype.h>

/*
Crie um programa que receba 5 nomes, com um máximo de 20 caracteres, sendo
que cada nome deverá ser guardado numa linha de uma matriz. 
Imprima os nomes recebidos (deverá utilizar uma matriz do tipo “char”).
*/

int main()
{
    setlocale(LC_ALL, "Portuguese");
    
    char nomes[5][20];

    for (int i = 0; i < 5; i++) {
        printf("Insira o nome nº %d: ", i + 1);
        fgets(nomes[i], sizeof(nomes[i]), stdin);

        nomes[i][strcspn(nomes[i], "\n")] = '\0';        
           	
    }
    
    printf("\n Nomes inseridos \n");
    for (int i = 0; i < 5; i++) {
        printf("%dº nome: %s \n", i + 1, nomes[i]);
    }
    
    return 0;
}