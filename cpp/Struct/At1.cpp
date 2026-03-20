#include <stdio.h>
#include <locale.h>
#include <string.h>

struct Pessoa {
    char nome[20];
    char morada[30];
    char telefone[10];
    int idade;
};

int main() {
    setlocale(LC_ALL, "Portuguese");

    struct Pessoa p[2];

    strcpy(p[0].nome, "Mike");
    strcpy(p[0].morada, "Rua do Alecrim");
    strcpy(p[0].telefone, "934553440");
    p[0].idade = 31;    
           
    strcpy(p[1].nome, "Carolina");
    strcpy(p[1].morada, "Conceição Fernandes");
    strcpy(p[1].telefone, "963779076");
    p[1].idade = 27;
              
    for (int i = 0; i < 2; i++) {
        printf("O seu nome é %s, com a morada %s, número de telefone %s e com idade de %d anos.\n",
               p[i].nome, p[i].morada, p[i].telefone, p[i].idade);
    }

    return 0;
}