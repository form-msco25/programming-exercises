"""Crie um tuplo com temperaturas diárias da semana e use in para
verificar se uma temperatura específica ocorreu; calcule depois a média
com sum() e len()."""
from random import randint
tup_temp = ()
inter = randint(5,10)
for i in range(inter):
    temp = randint(5,35)
    tup_temp = tup_temp + (temp,)
verif_temp = int(input("Digite a temperatura em graus Celsius que deseja verificar: "))
if verif_temp in tup_temp:
    print(f"A temperatura {verif_temp}º C está dentro do registo.")
else:
    print(f"A temperatura {verif_temp}º C não está dentro do registo.")
media_temp = sum(tup_temp)/len(tup_temp)
print(f"As temperaturas registadas são as seguintes: {tup_temp}\nA média é: {media_temp:.2f}º C")