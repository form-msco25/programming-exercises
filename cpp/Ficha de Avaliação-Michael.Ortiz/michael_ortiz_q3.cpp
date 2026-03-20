#include <stdio.h>
#include <locale.h>

/* Crie um programa que realize o cálculo do vencimento líquido de um funcionário
conforme uma tipologia de acordo com a seguinte tabela e que realize cálculos
até o utilizador inserir um tipo de funcionário = “99”. */

/* Nota:
• Receba do utilizador o tipo de funcionário.
• Utilize uma função para realizar o cálculo.
• Apresente os resultados com 2 casas decimais.
Tipo Vencimento Bruto IRS
1 1000€ 5%
2 1200€ 6%
3 1500€ 7% */

float liq(float brut, float irs){
	return brut - irs;
}

int main()
{
    setlocale (LC_ALL, "Portuguese");
    
    int tipo;
    float brut, irs, liquido;
    
    do{
    	printf("Digite o tipo de funcionário (1, 2, ou 3. 99 para finalizar o programa): \n");
    	scanf("%d", &tipo);
    	
    	if (tipo != 1 && tipo != 2 && tipo != 3){
			printf("Valor inválido! Tente novamente .\n");
		}
	}	
	while (tipo != 1 && tipo != 2 && tipo != 3);
	
	if (tipo == 1){
        brut = 1000;
        irs = brut * 0.05;
    } 
	else if (tipo == 2) {
        brut = 1200;
        irs = brut * 0.06;
    }
	else {
        brut = 1500;
        irs = brut * 0.07;
    }
	
	liquido = liq(brut, irs);
	
	printf("\nTipo de funcionário: %d\n", tipo);
    printf("Vencimento bruto: %.2f\n", brut);
    printf("Desconto IRS: %.2f\n", irs);
    printf("Vencimento líquido: %.2f\n", liquido);
	
    return 0;
}

