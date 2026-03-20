"""Crie um programa que calcule os números primos compreendidos no intervalo 1000 e 2000. 
Deve usar uma função chamada “primos” o qual, deverá ser o modulo de um ficheiro principal cujo nome será “primo.py”. 
O nome do ficheiro externo (modulo), deve ter o nome “funcoes.py”."""

def primos():
    num_primo = []
    for i in range(1000, 2001):
        primo_sim = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                primo_sim = False
        if primo_sim:
            num_primo.append(i)
    return num_primo