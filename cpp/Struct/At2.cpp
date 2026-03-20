#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>

struct Cliente{
	char nome[20];
	char email[20];
};

void adicCliente(Cliente clientes[], int *qtd);
void visualClientes(Cliente clientes[], int qtd);
void editCliente(Cliente clientes[], int qtd);
void exclCliente(Cliente clientes[], int *qtd);

void Adicionar() {
    printf("\nVocê escolheu a opção 1!\n");
}

void Visualizar() {
    printf("\nVocê escolheu a opção 2!\n");
}

void Editar() {
    printf("\nVocê escolheu a opção 3!\n");
}

void Excluir() {
    printf("\nVocê escolheu a opção 3!\n");
}

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    struct Cliente clientes[50];
    int qtdClientes = 0;
    int opcao;

    do {
        printf("\n========== MENU ==========\n");
        printf("1 - Adicionar Cliente\n");
        printf("2 - Visualizar Clientes\n");
        printf("3 - Editar Cliente\n");
        printf("4 - Excluir Cliente\n");
        printf("0 - Sair\n");
        printf("==========================\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar();

        switch (opcao) {
            case 1:
                adicCliente(clientes, &qtdClientes);
                break;
            case 2:
                visualClientes(clientes, qtdClientes);
                break;
            case 3:
                editCliente(clientes, qtdClientes);
                break;
            case 4:
                exclCliente(clientes, &qtdClientes);
                break;
            case 0:
                printf("Saindo do programa...\n");
                break;
            default:
                printf("Opção inválida!\n");
        }

        printf("\nPressione ENTER para continuar...");
        getchar();
        system("clear || cls");

    } while (opcao != 0);

    return 0;
}

void adicCliente(Cliente clientes[], int *qtd) {
    if (*qtd >= 50) {
        printf("Limite máximo de clientes atingido!\n");
        return;
    }

    Cliente novo;
    printf("Digite o nome do cliente: ");
    fgets(novo.nome, 20, stdin);
    novo.nome[strcspn(novo.nome, "\n")] = '\0';

    printf("Digite o email do cliente: ");
    fgets(novo.email, 20, stdin);
    novo.email[strcspn(novo.email, "\n")] = '\0';

    clientes[*qtd] = novo;
    (*qtd)++;

    printf("Cliente adicionado com sucesso!\n");
}

void visualClientes(Cliente clientes[], int qtd) {
    if (qtd == 0) {
        printf("Nenhum cliente cadastrado.\n");
        return;
    }

    printf("\n--- Lista de Clientes ---\n");
    for (int i = 0; i < qtd; i++) {
        printf("%d) Nome: %s | Email: %s\n", i + 1, clientes[i].nome, clientes[i].email);
    }
}

void editCliente(Cliente clientes[], int qtd) {
    if (qtd == 0) {
        printf("Nenhum cliente cadastrado para editar.\n");
        return;
    }

    int indice;
    visualClientes(clientes, qtd);
    printf("\nDigite o número do cliente que deseja editar: ");
    scanf("%d", &indice);
    getchar();

    if (indice < 1 || indice > qtd) {
        printf("Cliente inválido!\n");
        return;
    }
    
    indice--;
    printf("Novo nome: ");
    fgets(clientes[indice].nome, 20, stdin);
    clientes[indice].nome[strcspn(clientes[indice].nome, "\n")] = '\0';

    printf("Novo email: ");
    fgets(clientes[indice].email, 20, stdin);
    clientes[indice].email[strcspn(clientes[indice].email, "\n")] = '\0';

    printf("Cliente atualizado com sucesso!\n");
}

void exclCliente(Cliente clientes[], int *qtd) {
    if (*qtd == 0) {
        printf("Nenhum cliente cadastrado para excluir.\n");
        return;
    }

    int indice;
    visualClientes(clientes, *qtd);
    printf("\nDigite o número do cliente que deseja excluir: ");
    scanf("%d", &indice);
    getchar();

    if (indice < 1 || indice > *qtd) {
        printf("Cliente inválido!\n");
        return;
    }

    indice--;
    
    for (int i = indice; i < *qtd - 1; i++) {
        clientes[i] = clientes[i + 1];
    }
    (*qtd)--;

    printf("Cliente excluído com sucesso!\n");
}