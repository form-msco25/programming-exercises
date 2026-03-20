#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <ctype.h>     // Manipulação de caracteres
// 2 - Fazer uma cópia do ficheiro de texto para outro.

int main()
{
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português    
    
	FILE *fich1 = fopen ("texto.txt", "r");
	
	if (fich1 == NULL){
		printf("Não foi possível abrir o ficheiro.\n");
		return 1;
	}
	char texto1[1000];
	char temp[1000]="";
	while (fgets(texto1, sizeof(texto1), fich1) != NULL){	
	}
	temp = texto1;
	fclose(fich1);
	
	FILE *fich2 = fopen ("copia_texto.txt, w");
	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.");
		return 1;		
	}
	
	char texto2 [1000] = temp;
	
	for (int j=0; texto2[j] != '\0'; i++){
		fputc(texto2[j], fich2);
	}
	fclose(fich2);

    return 0;
}
