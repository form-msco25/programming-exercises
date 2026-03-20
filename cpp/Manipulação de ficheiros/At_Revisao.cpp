#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <ctype.h>     // Manipulação de caracteres

int main()
{
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português
    
	/*FILE *fich;
	fich = fopen ("texto.txt", "w");
		
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.\n");
		return 1;		
	}	
	fclose(fich);*/
	
	/*FILE *fich = fopen ("texto.txt", "a");	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.\n");
		return 1;
	}
	fprintf(fich, "%s", "Manipulação de ficheiros em C. \nO motivo pelo qual se torna fundamental a utilização de ficheiros resulta da necessidade de perpetuar os dados para além do ciclo de vida de um programa. \nIsto significa que os dados armazenados nas variáveis criadas pela execução do programa, residentes na memória principal que, como se sabe, é de natureza volátil, apenas se encontram disponíveis enquanto o programa está em execução. \nEste facto representa uma clara limitação à longevidade dos dados que, em última instância, ficam dependentes de termos o nosso programa em execução vinte e quatro horas por dia, pois caso o programa seja terminado ou o computador desligado tudo voltará ao ponto de partida. \nUma solução possível consiste na utilização de ficheiros, que pelo facto de serem armazenados em suportes secundários, não ficam dependentes do programa estar em execução ou de termos o nosso equipamento ligado. \nEm termos de tipos de ficheiros, e uma vez que vamos abordar os modos texto/binários, vamos considerar duas grandes áreas:");
	fclose(fich);*/
	
	FILE *fich = fopen ("texto.txt", "r");	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.");
		return 1;
	}
	char texto[1000];
	while (fgets(texto, sizeof(texto), fich) != NULL){
		printf("%s", texto);
	}	
	fclose(fich);
		
    return 0;
}

