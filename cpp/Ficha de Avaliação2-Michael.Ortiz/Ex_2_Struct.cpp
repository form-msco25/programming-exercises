#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <ctype.h>     // Manipulação de caracteres

// Indique as principais diferenças entre uma “struct” e uma “union”, 
// exemplificando cada uma delas.

struct Pessoa {
    char nome[20];
    char morada[30];
    char telefone[10];
    int idade;
};

int main(){
	
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português

    struct Pessoa p1;

    strcpy(p1.nome, "Mike");
    strcpy(p1.morada, "Rua do Alecrim");
    strcpy(p1.telefone, "934553440");
    p1.idade = 31;
	
	printf("O seu nome é %s, com a morada %s, número de telefone %s e com idade de %d anos.\n",
               p1.nome, p1.morada, p1.telefone, p1.idade);
	   
    return 0;
}
