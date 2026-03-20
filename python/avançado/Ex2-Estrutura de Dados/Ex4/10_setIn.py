"""Crie um set com nomes de alunos e verifique se um determinado nome está no
set usando o operador in."""

set = {"michael", "carolina", "tiago", "joana", "afonso", "carlos"}
nome = input("Digite o nome que deseja verificar que esteja na lista: ").lower()
if nome in set:
    print(f"O nome '{nome}' está na lista.")
else:
    print(f"O nome '{nome}' não está na lista.")