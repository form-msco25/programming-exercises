#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <stdlib.h> // Alocação de memória

// Qual a importância da alocação dinâmica de memória. 
//Exemplifique com um trecho de código, devidamente comentado, a sua implementação.

int main()
{
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português
	
	// São definidas as variáveis e o tamanho da matriz bidimensional
	int i, j;
	int lin = 5;
	int col = 50;		
	// A função 'mallorc' aloca na memória o número de bytes definidos pelo tamanho 'sizeof()'
	// Sendo necessário utilizar 'casting' devido ao retorno ser de tipo '*void'
	char *mat = (char*) malloc(lin*col * sizeof(char));
	// No caso de não haver espaço suficiente na memória a função irá retornar 'NULL'
	if (mat == NULL){
		printf("Erro ao alocar memória.\n");
		return 1;
	}
	// Este ciclo 'for' percorre todas as posições da matriz e coloca '0' em cada elemento 
	for (i=0; i<lin; i++){
		for (j=0; j<col; j++){
			mat[(i*col) + j] = 0;
		}
	}
	// É necessário um ciclo 'for' para introduzir os dados da matriz em cada espaço de memória
	for (i=0; i<lin; i++){
		printf("Digite o nome %d: ", i+1);
		fgets(&mat[i*col], col, stdin);
		
		mat[i*col + strcspn(&mat[i*col], "\n")] = '\0';
	}
	// Novamente é necessário utilizar um ciclo 'for', neste caso para imprimir os dados armazenados
	printf("\n--- Nomes armazenados ---\n");
	for (i=0; i<lin; i++){
		printf("Nome %d: %s\n", i + 1, &mat[i*col]);
	}
	// Liberta o espaço de memória alocado pelo apontador		
	free(mat);
		
    return 0;
}
