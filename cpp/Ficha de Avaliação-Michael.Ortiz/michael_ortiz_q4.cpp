#include <stdio.h>
#include <locale.h>

/* Crie um programa que receba 5 valores de temperaturas máximas e 5 mínimas,
correspondente à temperatura máxima e mínima de 5 locais, guardando as
mesmas em 2 vetores (máximas, mínimas). Calcule a média de cada local e
guarde a média calculada num novo vetor.
• Utilize uma função que recebe cada posição dos dois vetores (não o vetor
todo) e retorna a média dessa posição, guardando a seguir essa média na
mesma posição do vetor de médias e repetindo esse processo para as 5
temperaturas. Assinatura da função: float media(int, int); */

float media(int tmax, int tmin) {
    return (tmax + tmin) / 2.0;
}
int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int maximas[5], minimas[5];
    float medias[5];
    
    for (int i = 0; i < 5; i++) {
        printf("Digite a temperatura maxima do local %d: ", i + 1);
        scanf("%d", &maximas[i]);

        printf("Digite a temperatura minima do local %d: ", i + 1);
        scanf("%d", &minimas[i]);
    }
    
    for (int i = 0; i < 5; i++) {
        medias[i] = media(maximas[i], minimas[i]);
    }
    
    printf("\n Medias de temperatura por local \n");
    for (int i = 0; i < 5; i++) {
        printf("Local %d -> Max: %d°C | Min: %d°C | Media: %.1f°C\n",
               i + 1, maximas[i], minimas[i], medias[i]);
    }
    
    return 0;
}