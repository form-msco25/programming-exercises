"""Defina um dicionário com notas de alunos (nome: tuplo de 3 notas);
use in para verificar se um aluno existe e calcule a média das suas notas."""
notas_alunos = {"michael": (19, 18, 20), "steven": (20, 19, 18), "tiago": (18, 17, 19)}
aluno = input("Introduza o nome do aluno: ").lower()

if aluno in notas_alunos:
    notas = notas_alunos[aluno]
    media = sum(notas) / len(notas)
    print(f"Média de {aluno}: {media:.2f}")
else:
    print("Aluno não encontrado.")
