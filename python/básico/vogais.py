if __name__ == "__main__":

    palavra = "inconstitucional"
    vogais = ["a", "e", "i", "o", "u"]
    contador = 0

    for letra in palavra:        
        if letra in vogais:
            contador += 1
    print(f"A palavra tem {contador} vogais.")