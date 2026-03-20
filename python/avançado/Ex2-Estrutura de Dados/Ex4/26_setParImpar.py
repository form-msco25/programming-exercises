"""Crie um set com números pares de 0 a 20 e outro com números ímpares de 1 a
19. Mostre a união dos dois sets."""

set_par = set()
set_impar = set()

for par in range(0, 21, 2):
    set_par.add(par)
for impar in range(1, 20, 2):
    set_impar.add(impar)
print(f"A união dos valores é a seguinte: \n{set_par | set_impar}")