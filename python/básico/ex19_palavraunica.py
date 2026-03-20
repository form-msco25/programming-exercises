"""
Escreve um programa que:
Peça ao utilizador para introduzir uma frase.
Converta a frase numa coleção (set) de palavras únicas.
Verifique se o número de palavras únicas é maior do que 5:
Se for maior, mostre as palavras em ordem alfabética.
Caso contrário, mostre a quantidade de palavras repetidas que foram removidas
"""

if __name__ == "__main__":
    frase = input("Escreva uma frase: ").lower()
    palavras = frase.split()
    palavras_unicas = set(palavras)

    if len(palavras_unicas) > 5:
        ordem_alfabetica = sorted(palavras_unicas)        
        print(f"\nPalavras da frase em ordem alfabética {ordem_alfabetica}.\n")
    else:
        palavras_removidas = len(palavras) - len(palavras_unicas)
        print(f"\nPalavras únicas da frase: {palavras_unicas}.\n")
        print(f"{palavras_removidas} palavras foram removidas.\n")