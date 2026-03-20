#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <ctype.h>     // Manipulação de caracteres

int main()
{
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português
    
    return 0;
}