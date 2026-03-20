#include<stdio.h>
#include<locale.h>

int main() {
	
	setlocale (LC_ALL, "Portuguese");
	
	FILE *fich;
	fich = fopen ("texto.txt", "w");
	if (fich != NULL){
		printf("Ficheiro aberto com sucesso.");		
	}
	else {
		printf("Não foi possível abrir o ficheiro.");
	}
	fclose(fich);
	return 0;
}