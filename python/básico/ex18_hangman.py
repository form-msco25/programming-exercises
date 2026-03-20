"""Criação do Jogo do Hangman em Python

Descrição:

- Neste exercício, você vai desenvolver o jogo "Hangman" (Jogo da Forca) em Python. O objetivo do jogo é que o
jogador adivinhe uma palavra secreta letra por letra. O jogador tem um número limitado de tentativas para adivinhar
a palavra correta, e cada erro o aproxima de "ser enforcado". O jogo termina quando o jogador adivinha corretamente
todas as letras da palavra ou quando atinge o número máximo de erros permitidos.

Requisitos:

- Seleção da Palavra: O programa deve selecionar aleatoriamente uma palavra de uma lista pré-definida de palavras secretas.

- Interação com o Jogador: O programa deve exibir ao jogador uma versão da palavra secreta com as letras ainda não adivinhadas
substituídas por underscores (_). Por exemplo, se a palavra secreta for "PYTHON" e o jogador já adivinhou as letras "P" e "T",
o programa deve exibir P_T___.

- Entrada do Jogador: O programa deve solicitar ao jogador que adivinhe uma letra.

- Validação de Entrada: O programa deve garantir que o jogador insira uma única letra. Caso o jogador insira mais de uma letra
ou um caractere que não seja uma letra, o programa deve solicitar uma nova entrada.

- Adivinhação da Letra: Se a letra estiver na palavra secreta, o programa deve revelar todas as ocorrências dessa letra na palavra.
Caso contrário, deve contabilizar um erro.

- Contabilização de Erros: O jogador tem um número limitado de tentativas (por exemplo, 6 tentativas).
Cada erro reduz o número de tentativas restantes.

Condições de Vitória e Derrota:

- O jogador vence se adivinhar todas as letras da palavra secreta antes de esgotar o número de tentativas.
- O jogador perde se esgotar todas as tentativas sem adivinhar a palavra.
- Exibição do Estado do Jogo: Após cada tentativa, o programa deve exibir o estado atual da palavra (com letras adivinhadas e underscores)
e o número de tentativas restantes.

- Finalização do Jogo: Ao final do jogo, o programa deve exibir uma mensagem indicando se o jogador venceu ou perdeu e revelar a palavra
secreta. Deve, também, oferecer ao jogador a opção de jogar novamente.

Dicas e Sugestões:

- Considere usar uma lista para armazenar as letras adivinhadas e um conjunto para armazenar as letras erradas.
- Use a biblioteca random para selecionar aleatoriamente uma palavra da lista de palavras secretas."""

from random import choice

forca = [
    """
    _______
    |/      
    |      
    |      
    |       
    |      
    |
    |___
    """,
    """
    _______
    |/      |
    |      (_)
    |      
    |       
    |      
    |
    |___
    """,
    """
    _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
    |___
    """,
    """
    _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |      
    |
    |___
    """,
    """
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      
    |
    |___
    """,
    """
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / 
    |
    |___
    """,
    """
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    |___
    """
]

marcas = ["HONDA", "SMART", "VOLVO", "TOYOTA", "SUBARU", "MITSUBISHI", "SEAT", "NISSAN", "MAZDA", "SUZUKI"]
def jogo_forca(): 
    palavra_secreta = list(choice(marcas))    
    palavra_oculta = ["_" for i in palavra_secreta]
    letras_adivinhadas = []
    letras_erradas = []    
    tentativas_restantes = 6    

    while tentativas_restantes > 0 and "_" in palavra_oculta:
        erros = 6 - tentativas_restantes
        print("\n===========================")
        print(forca[erros])
        print("Palavra:", palavra_oculta)   
        print("Tentativas restantes:", tentativas_restantes)
        print("Letras erradas:", letras_erradas)
        print("Letras acertadas:", letras_adivinhadas)

        letra = input("Insira uma letra: ").upper()

        if (len(letra) != 1 or not letra.isalpha()):
            print("Entrada inválida! Insira apenas UMA LETRA!")
            continue
        elif letra in letras_adivinhadas or letra in letras_erradas:
            print("Já tentou essa letra!")
            continue
        elif letra in palavra_secreta:
            letras_adivinhadas.append(letra)
            print("Boa! A letra está na palavra.")
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_oculta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas_restantes -= 1
            print("Letra errada!")            
    print("\n===========================")
    
    if "_" not in palavra_oculta:
        print("PARABÉNS! Adivinhou a palavra: ", palavra_secreta)
    else:
        print(forca[6])
        print("FIM DO JOGO! A palavra era: ", palavra_secreta)

if __name__ == "__main__":
    cond = True
    while cond:
        jogo_forca()
        jogar_novamente = input("\nDeseja jogar novamente? (S/N): ").upper()
        if jogar_novamente != "S":
            print("Obrigado por participar! Volte sempre!")
            cond = False