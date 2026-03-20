"""Cria um programa em Python que simule a retirada de uma carta de um baralho.
Para isso, começa por criar uma lista com algumas cartas (por exemplo: "Ás de Copas", "Rei de Espadas", "10 de Ouros", "2 de Paus", etc.).

O programa deve:
Importar o módulo random.
Escolher aleatoriamente uma carta da lista que representa o baralho.
Verificar, usando uma estrutura if/else, se a carta sorteada é um Ás.
Se for um Ás, o programa deve exibir a mensagem: "Saiu um Ás! Boa sorte!"
Caso contrário, deve mostrar: 'A carta sorteada foi: <carta>"."""

import random

if __name__ == "__main__":

    lista = ["Ás de Copas", "Rei de Espadas", "10 de Ouros", "2 de Paus", "Ás de Espadas", "Ás de Ouros", "Ás de Paus", "7 de Copas", "9 de Copas", "8 de Espadas", "7 de Ouros", "9 de Paus"]
    carta = random.choice(lista)

    if carta=="Ás de Copas" or carta=="Ás de Espadas" or carta=="Ás de Ouros" or carta=="Ás de Paus":
        print("Saiu um Ás! Boa sorte!")
    else:
        print(f"A carta sorteada é {carta}")

