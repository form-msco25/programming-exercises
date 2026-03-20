#include <stdio.h>
#include <locale.h>

/* Receba um valor inteiro para a variável n;
Seguidamente, crie um apontador p para essa variável.
Imprima o conteúdo de n, usando acesso direto e indireto.
Imprima os endereços de memória das duas variáveis e o conteúdo do apontador p. */

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int n;
    int *p;
    
    printf("Digite um valor inteiro: ");
    scanf("%d", &n);
    
    p = &n;
    
    printf("\nConteúdo de n (acesso direto): %d", n);
    printf("\nConteúdo de n (acesso indireto via ponteiro): %d", *p);
    
    printf("\n\nEndereço de n: %p", &n);
    printf("\nEndereço do ponteiro p: %p", &p);
    
    printf("\nConteúdo do ponteiro p (endereço armazenado): %p\n", p);
    
    return 0;
}