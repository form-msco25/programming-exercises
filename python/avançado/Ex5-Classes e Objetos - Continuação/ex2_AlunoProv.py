"""### Descrição
Crie um sistema para gerenciar as notas de um aluno em diferentes provas e
calcular seu desempenho final.
### Atributos
- `nome` (string): nome do aluno
- `matricula` (string): número de matrícula
- `provas` (lista): lista de provas, cada prova tem 3 notas [nota1, nota2, nota3]
### Métodos Obrigatórios
**`__init__(nome, matricula)`**
- Inicializa o aluno
- Começa com lista de provas vazia
**`adicionar_prova(notas)`**
- Recebe uma lista com 3 notas [nota1, nota2, nota3]
- Cada nota deve estar entre 0 e 20
- Valida se a lista tem exatamente 3 elementos
- Adiciona à lista de provas se válido
**`media_geral()`**
- Calcula a média de TODAS as notas de TODAS as provas
- Retorna um número float
- Se não há provas, retorna 0
**`conceito_final()`**
- Retorna o conceito baseado na média geral:
- 'A' se média >= 14
- 'B' se média >= 11 e < 14
- 'C' se média >= 9 e < 11
- 'R' se média < 9"""

class AlunoProvas:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.provas = []
    def adicionar_prova(self, notas):        
        if not isinstance(notas, list) or len(notas) != 3:
            raise ValueError("A prova deve conter exatamente 3 notas.")
        for nota in notas:
            if not isinstance(nota, (int, float)) or nota < 0 or nota > 20:
                raise ValueError("Cada nota deve estar entre 0 e 20.")
        self.provas.append(notas)
    def media_geral(self):
        if not self.provas:
            return 0.0
        total = 0
        quantidade = 0
        for prova in self.provas:
            for nota in prova:
                total += nota
                quantidade += 1
        return total / quantidade
    def conceito_final(self):
        media = self.media_geral()
        if media >= 14:
            return 'A'
        elif media >= 11:
            return 'B'
        elif media >= 9:
            return 'C'
        else:
            return 'R'
# Teste 1: Criar aluno e adicionar prova
aluno = AlunoProvas("João Silva", "2024001")
aluno.adicionar_prova([12, 14, 13])
print(aluno.media_geral()) # Esperado: 13.0
print(aluno.conceito_final()) # Esperado: B
# Teste 2: Múltiplas provas
aluno = AlunoProvas("Maria Santos", "2024002")
aluno.adicionar_prova([10, 12, 11])
aluno.adicionar_prova([14, 15, 16])
print(aluno.media_geral()) # Esperado: 13.0
print(aluno.conceito_final()) # Esperado: B
# Teste 3: Notas altas (conceito A)
aluno = AlunoProvas("Pedro Costa", "2024003")
aluno.adicionar_prova([15, 16, 17])
print(aluno.conceito_final()) # Esperado: A
# Teste 4: Notas baixas (conceito R)
aluno = AlunoProvas("Ana oliveira", "2024004")
aluno.adicionar_prova([5, 6, 7])
print(aluno.conceito_final()) # Esperado: R
# Teste 5: Validação de notas inválidas
aluno = AlunoProvas("Teste", "0000")
aluno.adicionar_prova([10, 25, 8]) # Nota 25 é inválida
print(len(aluno.provas)) # Esperado: 0 (não foi adicionada)