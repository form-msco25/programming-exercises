#include<stdio.h>
#include<locale.h>
#include <string.h>
/* 1 - Escrever num ficheiro de texto "caracter-a-caracter", a seguinte frase: 
"Manipulação de ficheiros em c";
2 - Acrescentar ao ficheiro anterior a seguinte linha completa, 
"É possível escrever uma linha completa de texto".
3 - Escreva num ficheiro de texto os dados de uma instância da "struct" Funcionario, 
cujos campos são: codigo, nome, funcao;
4 - Leia o ficheiro escrito anteriormente para outra 
"instância" da "struct" Funcionario.*/
typedef struct {
	int codigo;
	char nome[40]; 
	char funcao[20];
} Funcionario;

int main() {
	
	setlocale (LC_ALL, "Portuguese");
	
	/* 1.-
	FILE *fich;
	fich = fopen ("texto.txt", "w");
	char frase[] = "Manipulação de ficheiros em c.";
	int i;	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.");
		return 1;		
	}
	for (i=0; frase[i] != '\0'; i++){
		fputc(frase[i], fich);
	}	s
	fclose(fich); */
	
	/* 2.-
	FILE *fich = fopen ("texto.txt", "a");	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.");
		return 1;
	}
	fprintf (fich, "%s", "\nÉ possível escrever uma linha completa de texto.");
	fclose(fich); */
	
	/* 3.-
	FILE *fich = fopen ("texto.txt", "a");	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.");
		return 1;
	}	
	Funcionario f;	
	f.codigo = 31;
	strcpy(f.nome, "Mike");
	strcpy(f.funcao, "Técnico");	
	fprintf(fich, "\nCódigo: %d\nNome: %s\nFunção: %s\n", f.codigo, f.nome, f.funcao);	
	fclose(fich); */
	
	/*4.-*/
	FILE *fich = fopen ("texto.txt", "r");	
	if (fich == NULL){
		printf("Não foi possível abrir o ficheiro.");
		return 1;
	}	
	Funcionario f;	
	fscanf(fich, "Código: %d\nNome: %s\nFunção: %s\n", &f.codigo, f.nome, f.funcao);
	printf("Código: %d\nNome: %s\nFunção: %s\n", &f.codigo, f.nome, f.funcao);	
	fclose(fich);
	
	return 0;
}