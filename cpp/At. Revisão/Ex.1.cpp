#include <stdio.h>
#include <locale.h> 
#include <stdbool.h> // bool

// Escreva um programa em C que verifique se três inteiros dados pelo utilizador, estão no intervalo de 20 a 50 (inclusive)
// e retorne true se pelo menos um deles estiver dentro do intervalo. Se nenhum dos inteiros estiver dentro do intervalo, o programa retorna false.
// Nota: use uma função par testar os números).

bool intervalo(int n) {
    return (n >= 20 && n <= 50);
}

int main() {
	
	setlocale (LC_ALL, "Portuguese");
	
    int a, b, c;

    printf("Digite tres numeros inteiros: ");
    scanf("%d %d %d", &a, &b, &c);
    
    if (intervalo(a) || intervalo(b) || intervalo(c)) {
        printf("true\n");
    } else {
        printf("false\n");
    }

    return 0;
}
