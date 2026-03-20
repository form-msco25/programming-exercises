"""Crie um tuplo com 5 números e calcule a soma dos valores usando a função
sum."""

t = ()
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    t = t + (num,)
print(f"Tupla: {t}")
print(f"A soma dos valores da tupla é: {sum(t)}")