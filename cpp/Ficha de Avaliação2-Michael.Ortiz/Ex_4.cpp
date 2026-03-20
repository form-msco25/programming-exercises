#include <stdio.h>     // Suporte às funções de entrada/saida
#include <locale.h> // Suporte à função setlocale
#include <string.h> // Manipulação de strings
#include <stdlib.h> // Alocação de memória

/*Crie um programa que responda aos seguintes requisitos:
	a. Pretende-se guardar os dados dos jogadores de uma equipa (número,
	nome, posição);
	b. Pretende-se guardar todos os jogadores numa equipa que deverá
	guardar igualmente o nome, cor do equipamento, posição no
	campeonato);
	c. Imprima todos os jogadores, mencionando a equipa a que pertencem.
	d. Guarde os dados que imprimiu no ecrã num ficheiro binário.
*/

#define MAX_JOGADORES 50

typedef struct {
    int numero;
    char nome[50];
    char posicao[30];
} Jogador;

typedef struct {
    char nome[50];
    char corEquipamento[30];
    int posicaoCampeonato;
    int totalJogadores;
    Jogador jogadores[MAX_JOGADORES];
} Equipa;

int main()
{
    setlocale (LC_ALL, "Portuguese"); // Acerto do mapa de caracteres e demais definições regionais para português

    Equipa equipa;

    strcpy(equipa.nome, "RCD Mallorca");
    strcpy(equipa.corEquipamento, "Vermelho e Preto");
    equipa.posicaoCampeonato = 3;
    equipa.totalJogadores = 4;
	
	equipa.jogadores[0].numero = 1;
    strcpy(equipa.jogadores[0].nome, "Miguel Moyà");
    strcpy(equipa.jogadores[0].posicao, "Guarda-Redes");
    
    equipa.jogadores[1].numero = 4;
    strcpy(equipa.jogadores[1].nome, "José Nunes");
    strcpy(equipa.jogadores[1].posicao, "Defesa");
    
    equipa.jogadores[2].numero = 6;
    strcpy(equipa.jogadores[2].nome, "Michael Ortiz");
    strcpy(equipa.jogadores[2].posicao, "Meio-campo");
    
    equipa.jogadores[3].numero = 9;
    strcpy(equipa.jogadores[3].nome, "Dani Güiza");
    strcpy(equipa.jogadores[3].posicao, "Avançado");

    printf("Equipa: %s\n", equipa.nome);
    printf("Cor do equipamento: %s\n", equipa.corEquipamento);
    printf("Posição no campeonato: %d\n\n", equipa.posicaoCampeonato);

    for (int i = 0; i < equipa.totalJogadores; i++) {
        printf("Jogador %d\n", i + 1);
        printf("Número: %d\n", equipa.jogadores[i].numero);
        printf("Nome: %s\n", equipa.jogadores[i].nome);
        printf("Posição: %s\n", equipa.jogadores[i].posicao);
        printf("Equipa: %s\n\n", equipa.nome);
    }

    FILE *fich = fopen("equipa.bin", "wb");
    
    if (fich == NULL) {
        printf("Erro ao criar o ficheiro.\n");
        return 1;
    }

    fwrite(&equipa, sizeof(Equipa), 1, fich);
    fclose(fich);

    printf("Dados guardados com sucesso no ficheiro 'equipa.bin'.\n");

    return 0;
}
