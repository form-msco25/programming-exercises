"""Crie uma classe `ContaBancaria` com os seguintes atributos:
- `numero_conta` (string)
- `titular` (string)
- `saldo` (float)
- `tipo_conta` (string: "Corrente" ou "Poupança")
- `historico` (lista de operações)
Implemente os seguintes métodos:
- `depositar(valor)`: adiciona valor ao saldo e regista no histórico
- `sacar(valor)`: subtrai valor do saldo (se houver saldo) e regista no histórico
- `transferir(outra_conta, valor)`: transfere valor para outra conta e regista em
ambos os históricos
- `exibir_historico()`: imprime todas as operações realizadas
- `exibir_saldo()`: imprime o saldo atual
**Teste:** Crie duas contas, realize depósitos, saques e uma transferência. Exiba o
histórico de ambas."""

class ContaBancaria:
    def __init__(self, num_conta, titular, saldo, tipo_conta):
        self.num_conta = num_conta
        self.titular = titular 
        self.saldo = saldo 
        self.tipo_conta = tipo_conta        
        self.historico = []
    def depositar(self, valor):        
        self.saldo += valor        
        self.historico.append(f"Depósito de: {valor:.2f}")
    def levantar(self, valor):        
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(f"Levantamento de: {valor:.2f}")
        else:
            print("Saldo insuficiente para levantamento.")
    def transferir(self, outra_conta, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            outra_conta.saldo += valor
            self.historico.append(f"Transferência enviada de {valor:.2f} para a conta {outra_conta.num_conta}")
            outra_conta.historico.append(f"Transferência recebida de {valor:.2f} da conta {self.num_conta}")
        else:
            print("Saldo insuficiente para transferência.")
    def exibir_historico(self):
        print(f"\nHistórico da conta {self.num_conta}. Sr.(a) {self.titular}:")
        for operacao in self.historico:
            print("-", operacao)
    def exibir_saldo(self):
        print(f"Saldo atual: {self.saldo:.2f}")

conta1 = ContaBancaria(1234, "Michael", 0, "Corrente")
conta2 = ContaBancaria(5678, "Steven", 0, "Corrente")

conta1.depositar(75)
conta1.levantar(50)

conta2.depositar(50)
conta2.levantar(75)

conta1.transferir(conta2, 20)

conta1.exibir_historico()
conta1.exibir_saldo()

conta2.exibir_historico()
conta2.exibir_saldo()