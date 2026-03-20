"""A empresa "TechStore" está a lançar uma promoção com códigos promocionais. Cada código é composto por:

Um prefixo "PROMO" (em letras maiúsculas),
seguido de um traço "-",
e um número de 4 dígitos (ex: PROMO-1234).

Crie um programa em Python que:

1.Solicite ao utilizador a introdução de um código promocional (pode conter espaços no início ou fim).

2.Limpe os espaços em branco desnecessários.

3.Valide se o código começa com "PROMO-". Dica: podes utilizar o slicing ou a função startswith()

4.Se começar com "PROMO-", verifique:
Se a parte numérica tem exatamente 4 dígitos.
Se todos os caracteres após o traço são dígitos.


5.Caso tudo esteja correto, mostre:
"Código válido. Desconto aplicado!"
Caso contrário, mostre mensagens de erro apropriadas como:
"Código inválido: não começa com 'PROMO-'."
"Código inválido: a parte numérica deve ter 4 dígitos."
"Código inválido: a parte numérica contém caracteres não numéricos."
Pesquisa sobre as funções que estão na imagem e entende como deves utiliza-las!"""

if __name__ == "__main__":

    var = True
    while var:
        cod = input("Insira o código promocional: ").strip()
        num = cod[6:10]
        if len(cod) == 10: 
            if cod.startswith('PROMO-'):
                if cod[6:10].isdigit():
                    print("Código válido. Desconto aplicado!")
                else:
                    print("Código inválido: a parte numérica deve ter 4 dígitos.")
            else:
                print("Código inválido: não começa com 'PROMO-'.")                
        else:            
            print("Código inválido: tem de ter 10 caracteres.")
