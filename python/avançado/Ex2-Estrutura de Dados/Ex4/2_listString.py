"""Dada a string 'programacao em python', use o operador in para verificar se o
caractere 'a' aparece na frase."""

string = "Programacao em Python"
lista = list(string)
letra = "a"
if letra in lista:
    print(f"A letra '{letra}' está na frase:\n{lista}")
else:
    print(f"A letra {letra} não está na frase:\n{lista}")