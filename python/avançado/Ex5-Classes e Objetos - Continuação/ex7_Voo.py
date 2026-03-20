"""### Descrição
Simule um sistema de controle de voos com passageiros.
### Atributos
- `numero` (string): número do voo (ex: "AA100")
- `destino` (string): cidade destino
- `passageiros_max` (int): capacidade máxima
- `passageiros_atuais` (list): lista de nomes dos passageiros embarcados
### Métodos Obrigatórios
**`__init__(numero, destino, passageiros_max)`**
- Inicializa voo
- Lista de passageiros começa vazia
**`embarcar(nome)`**
- Adiciona passageiro
- Valida se há vagas
- Valida se passageiro já embarcou
- Retorna True se sucesso, False se falhou
**`desembarcar(nome)`**
- Remove passageiro
- Retorna True se removido, False se não encontrado
**`vagas_disponiveis()`**
- Retorna número de vagas vazias
**`lotacao_percentual()`**
- Retorna percentual de ocupação
- Exemplo: 80.5
**`status_voo()`**
- Retorna string:
- "Voo lotado" se cheio
- "Vagas disponíveis" se há espaço
- "Voo deserto" se vazio"""

class Voo:
    def __init__(self, numero, destino, passageiros_max):
        self.numero = numero
        self.destino = destino
        self.passageiros_max = int(passageiros_max)
        self.passageiros_atuais = []
    def embarcar(self, nome):
        if len(self.passageiros_atuais) >= self.passageiros_max:
            return False  # voo cheio
        if nome in self.passageiros_atuais:
            return False  # passageiro já embarcou
        self.passageiros_atuais.append(nome)
        return True
    def desembarcar(self, nome):
        if nome in self.passageiros_atuais:
            self.passageiros_atuais.remove(nome)
            return True
        return False
    def vagas_disponiveis(self):
        return self.passageiros_max - len(self.passageiros_atuais)
    def lotacao_percentual(self):
        if self.passageiros_max == 0:
            return 0.0
        return (len(self.passageiros_atuais) / self.passageiros_max) * 100
    def status_voo(self):
        ocupacao = len(self.passageiros_atuais)
        if ocupacao == 0:
            return "Voo deserto"
        elif ocupacao >= self.passageiros_max:
            return "Voo lotado"
        else:
            return "Vagas disponíveis"
# Teste 1: Criar voo e embarcar passageiros
voo = Voo("AA100", "Lisboa", 5)
voo.embarcar("João")
voo.embarcar("Maria")
voo.embarcar("Pedro")
print(voo.vagas_disponiveis()) # Esperado: 2
# Teste 2: Status do voo
print(voo.status_voo()) # Esperado: "Vagas disponíveis"
# Teste 3: Lotação percentual
print(voo.lotacao_percentual()) # Esperado: 60.0
# Teste 4: Voo lotado
voo.embarcar("Ana")
voo.embarcar("Carlos")
print(voo.status_voo()) # Esperado: "Voo lotado"
# Teste 5: Desembarque
voo.desembarcar("João")
print(voo.vagas_disponiveis()) # Esperado: 1
print(voo.status_voo()) # Esperado: "Vagas disponíveis"
# Teste 6: Passageiro duplicado
resultado = voo.embarcar("Maria") # Já embarcou
print(resultado) # Esperado: False