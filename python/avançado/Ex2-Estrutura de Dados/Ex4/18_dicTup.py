"""Crie um dicionário em que as chaves são nomes de alunos e os valores são
tuplos com (nota1, nota2). Calcule a média de cada aluno."""

aluno_notas = {"michael" : (16.0, 18.0), "steven" : (17.0, 19.0)}
for aluno, notas in aluno_notas.items():
    media = sum(notas) / len(notas)    
    print(f"{aluno}: média = {media:.2f}")