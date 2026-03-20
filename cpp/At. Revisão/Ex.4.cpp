#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

// Escreva um programa que verifique se duas strings são iguais, sem utilizar a função “strcmp”.
// Nota: Desenvolva uma função que verifique as strings e devolve 0 se forem diferentes e 1 se forem iguais.

int comp_str(char s1[], char s2[]) {
    int i = 0;

    while (s1[i] != '\0' && s2[i] != '\0') {
        if (s1[i] != s2[i]) {
            return 0;
        }
        i++;
    }

    if (s1[i] == '\0' && s2[i] == '\0')
        return 1;
    else
        return 0;
}

int main() {
	
	setlocale (LC_ALL, "Portuguese");
	
    char str1[20], str2[20];

    printf("Digite a primeira string: ");
    fgets(str1, sizeof(str1), stdin);

    printf("Digite a segunda string: ");
    fgets(str2, sizeof(str2), stdin);

    int i = 0;
    while (str1[i] != '\0') {
        if (str1[i] == '\n') str1[i] = '\0';
        i++;
    }
    i = 0;
    while (str2[i] != '\0') {
        if (str2[i] == '\n') str2[i] = '\0';
        i++;
    }

    if (comp_str(str1, str2))
        printf("As strings são IGUAIS.\n");
    else
        printf("As strings são DIFERENTES.\n");

    return 0;
}