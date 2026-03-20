#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>
/* Crie um programa que utilize uma struct "aluno", 
com os campos, id,  nome, email, media_final. */

// Crie dois alunos utilizando a alocação dinâmica de memória.

typedef struct {
	int id;
	char nome[40];
	char email[40];
	float media_final;
} Aluno;

int main(){
	setlocale(LC_ALL, "Portuguese");
	
	Aluno *a1 = (Aluno*) malloc(sizeof(Aluno));
	if (a1 == NULL){
        printf("Erro ao alocar memória!\n");
        return 1;
    }
    
	a1->id=1;
	strcpy(a1->nome, "Michael Ortiz");
	strcpy(a1->email, "michael_ortiz@email.com");
	a1->media_final=18.5;
		
	Aluno *a2 = (Aluno*) malloc(sizeof(Aluno));
	if (a2 == NULL){
        printf("Erro ao alocar memória!\n");
        free(a1);
        return 1;
    }
    
	a2->id=2;
	strcpy(a2->nome, "Carolina Pereira");
	strcpy(a2->email, "carol_per@email.com");
	a2->media_final=18.0;
	
	printf("Aluno 1:\nID: %d\nNome: %s\nEmail: %s\nMédia: %.2f\n\n",
           a1->id, a1->nome, a1->email, a1->media_final);

    printf("Aluno 2:\nID: %d\nNome: %s\nEmail: %s\nMédia: %.2f\n\n",
           a2->id, a2->nome, a2->email, a2->media_final);
           
    free(a1);
    free(a2);
	
	return 0;
}