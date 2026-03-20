#include <stdio.h>
#include <locale.h>
#include <string.h>


union Pessoa {
    char nome[100];
    char morada[150];
    char telefone[20];
    int idade;
};

int main() {
	setlocale(LC_ALL, "Portuguese");
	
    union Pessoa pessoa1, pessoa2;

    printf("=== Primeira Pessoa ===\n");
    printf("Nome: ");
    fgets(pessoa1.nome, sizeof(pessoa1.nome), stdin);

    printf("Morada: ");
    fgets(pessoa1.morada, sizeof(pessoa1.morada), stdin);

    printf("Telefone: ");
    fgets(pessoa1.telefone, sizeof(pessoa1.telefone), stdin);

    printf("Idade: ");
    scanf("%d", &pessoa1.idade);
    getchar();

    printf("\n=== Segunda Pessoa ===\n");
    printf("Nome: ");
    fgets(pessoa2.nome, sizeof(pessoa2.nome), stdin);

    printf("Morada: ");
    fgets(pessoa2.morada, sizeof(pessoa2.morada), stdin);

    printf("Telefone: ");
    fgets(pessoa2.telefone, sizeof(pessoa2.telefone), stdin);

    printf("Idade: ");
    scanf("%d", &pessoa2.idade);


    printf("\n=== Pessoa 1 (apenas último valor é válido) ===\n");
    printf("Idade: %d\n", pessoa1.idade);

    printf("\n=== Pessoa 2 (apenas último valor é válido) ===\n");
    printf("Idade: %d\n", pessoa2.idade);

    return 0;
}
