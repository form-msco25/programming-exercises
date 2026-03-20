"""Escreva um programa que leia uma frase do utilizador e use in para verificar se
a palavra 'python' aparece na frase, independentemente de
maiúsculas/minúsculas."""

frase = input("Introduza uma frase: ").lower()
palavra = "python"
if palavra in frase.split():
    print(f"A palavra '{palavra}' encontra-se na sua frase.")
else:
    print(f"A palavra '{palavra}' não encontra-se na sua frase.")