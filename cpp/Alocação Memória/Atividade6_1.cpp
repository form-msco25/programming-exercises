#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>
/* Crie um programa que possibilite guardar numa matriz de 5 nomes 
com comprimento máximo de 50 caracteres. 
Faça uso da alocação dinâmica de memória.*/ 
int main()
{
    setlocale (LC_ALL, "Portuguese");
		int i, j;
		int lin = 5;
		int col = 50;		
		
		char *mat = (char*) malloc(lin*col * sizeof(char));
		
		if (mat == NULL){
			printf("Erro ao alocar memória.\n");
			return 1;
		}
		for (i=0; i<lin; i++){
			for (j=0; j<col; j++){
				mat[(i*col) + j] = 0;
			}
		}
		for (i=0; i<lin; i++){
			printf("Digite o nome %d: ", i+1);
			fgets(&mat[i*col], col, stdin);
			
			mat[i*col + strcspn(&mat[i*col], "\n")] = '\0';
		}
		printf("\n--- Nomes armazenados ---\n");
		for (i=0; i<lin; i++){
			printf("Nome %d: %s\n", i + 1, &mat[i*col]);
		}		
		free(mat);
			
    return 0;
}
