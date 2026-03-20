#include <stdio.h>
#include <locale.h>

// Troque o conteúdo de 2 variáveis usando apontadores;

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int n1,n2;
    int *p1, *p2, *temp;   
    
    printf("Digite dois valores inteiros: ");
    scanf("%d%d", &n1, &n2);
    
    p1 = &n1;
    p2 = &n2;
    printf("\nO primeiro valor: %d, o segundo valor: %d", *p1, *p2);
    
    temp = p1;
    p1 = p2;
    p2 = temp;
    
    printf("\nALTERAÇÃO --> O primeiro valor: %d, o segundo valor: %d", *p1, *p2);
    
    
    return 0;
}