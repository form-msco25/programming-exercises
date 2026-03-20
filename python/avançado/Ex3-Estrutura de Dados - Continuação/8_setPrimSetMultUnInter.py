"""Gere um set de números primos até 20; crie outro set de múltiplos de 3
até 20 e mostre a união e interseção."""
primos = set()
for num in range(2, 21):
    num_primo = True
    for i in range(2, num):
        if num % i == 0:
            num_primo = False            
    if num_primo:
        primos.add(num)
multiplos_3 = {num for num in range(1, 21) if num % 3 == 0}
print("Primos até 20:", primos)
print("Múltiplos de 3 até 20:", multiplos_3)
uniao = primos | multiplos_3
print("União:", uniao)
intersecao = primos & multiplos_3
print("Interseção:", intersecao)