"""### Descrição
Gerencie vendedores com cálculo de comissões baseadas em metas.
### Atributos
- `nome` (string): nome do vendedor
- `vendas_mes` (float): valor total vendido no mês (começa em 0)
- `meta_mes` (float): meta de vendas para o mês
- `percentual_comissao` (float): percentual de comissão (ex: 5 para 5%)
### Métodos Obrigatórios
**`__init__(nome, meta, percentual_comissao)`**
- Inicializa vendedor
- Vendas começam em 0
**`registrar_venda(valor)`**
- Adiciona uma venda ao total do mês
- Valor deve ser positivo
**`calcular_comissao()`**
- Calcula comissão apenas sobre vendas ACIMA da meta
- Se vendas <= meta, comissão é 0
- Fórmula: (vendas - meta) × percentual_comissao / 100
- Retorna valor float
**`atingiu_meta()`**
- Retorna True se vendas_mes >= meta_mes
- Retorna False caso contrário
**`exibir_relatorio()`**
- Imprime relatório completo com:
- Nome do vendedor
- Meta de vendas
- Vendas realizadas
- Percentual de meta atingido (%)
- Atingiu meta? (Sim/Não)
- Comissão a receber (R$)"""

class Vendedor:
    def __init__(self, nome, meta, percentual_comissao):
        self.nome = nome
        self.meta_mes = float(meta)
        self.percentual_comissao = float(percentual_comissao)
        self.vendas_mes = 0.0
    def registrar_venda(self, valor):
        if valor <= 0:
            raise ValueError("O valor da venda deve ser positivo.")
        self.vendas_mes += valor
    def calcular_comissao(self):
        if self.vendas_mes <= self.meta_mes:
            return 0.0
        excedente = self.vendas_mes - self.meta_mes
        return excedente * self.percentual_comissao / 100
    def atingiu_meta(self):
        return self.vendas_mes >= self.meta_mes
    def exibir_relatorio(self):
        percentual_meta = (
            (self.vendas_mes / self.meta_mes) * 100
            if self.meta_mes > 0 else 0
        )
        print("------ RELATÓRIO DE VENDAS ------")
        print(f"Vendedor: {self.nome}")
        print(f"Meta do mês: R$ {self.meta_mes:.2f}")
        print(f"Vendas realizadas: R$ {self.vendas_mes:.2f}")
        print(f"Percentual da meta atingido: {percentual_meta:.2f}%")
        print(f"Atingiu meta? {'Sim' if self.atingiu_meta() else 'Não'}")
        print(f"Comissão a receber: R$ {self.calcular_comissao():.2f}")
        print("----------------------------------")
# Teste 1: Venda que atinge a meta
vendedor = Vendedor("João", 10000, 5)
vendedor.registrar_venda(6000)
vendedor.registrar_venda(5500)
print(vendedor.atingiu_meta()) # Esperado: True
print(vendedor.calcular_comissao()) # (11500-10000)*0.05 = 75.0
# Teste 2: Venda abaixo da meta
vendedor = Vendedor("Maria", 10000, 5)
vendedor.registrar_venda(8000)
print(vendedor.atingiu_meta()) # Esperado: False
print(vendedor.calcular_comissao()) # Esperado: 0.0
# Teste 3: Múltiplas vendas
vendedor = Vendedor("Pedro", 5000, 10)
vendedor.registrar_venda(1000)
vendedor.registrar_venda(2000)
vendedor.registrar_venda(3000)
print(vendedor.vendas_mes) # Esperado: 6000
print(vendedor.calcular_comissao()) # (6000-5000)*0.1 = 100.0
# Teste 4: Relatório completo
vendedor = Vendedor("Ana", 15000, 8)
vendedor.registrar_venda(18000)
vendedor.exibir_relatorio()