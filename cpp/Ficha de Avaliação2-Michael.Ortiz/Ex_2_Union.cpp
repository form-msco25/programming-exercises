#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <ctype.h>     // Manipulação de caracteres

// Indique as principais diferenças entre uma “struct” e uma “union”, 
// exemplificando cada uma delas.

union Pessoa {
    char nome[100];
    char morada[150];
    char telefone[20];
    int idade;
};

int main(){
	
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português

    union Pessoa pessoa1;

    strcpy(pessoa1.nome, "Mike");
    strcpy(pessoa1.morada, "Rua do Alecrim");
    strcpy(pessoa1.telefone, "934553440");
    pessoa1.idade = 31;
	
	printf("\n=== Pessoa 1 (apenas último valor é válido) ===\n");
    printf("Idade: %d\n", pessoa1.idade);
	printf("O seu nome é %s, com a morada %s, número de telefone %s e com idade de %d anos.\n",
               pessoa1.nome, pessoa1.morada, pessoa1.telefone, pessoa1.idade);

    return 0;
}
