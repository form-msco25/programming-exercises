"""Crie dois sets: um com vogais e outro com consoantes de uma frase
introduzida pelo utilizador; mostre a diferença simétrica entre eles."""

frase = list(input("Introduza uma frase: ").lower())
vogais = {"a", "e", "i", "o", "u"}
set_vogais = set()
set_consoantes = set()

for letra in frase:
    if letra.isalpha():
        if letra in vogais:
            set_vogais.add(letra)
        else:
            set_consoantes.add(letra)

print(f"Vogais da frase digitada: {set_vogais}")
print(f"COnsoantes da frase digitada: {set_consoantes}")
print(f"A diferença simétrica entre os dois: {set_vogais ^ set_consoantes}")