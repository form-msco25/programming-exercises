"""Crie um programa que calcule os números primos compreendidos no intervalo 1000 e 2000. 
Deve usar uma função chamada “primos” o qual, deverá ser o modulo de um ficheiro principal cujo nome será “primo.py”. 
O nome do ficheiro externo (modulo), deve ter o nome “funcoes.py”."""

from funcoes import primos

if __name__=="__main__":
    num = primos()
    print(f"Números primos entre 1000 e 2000: {num}")