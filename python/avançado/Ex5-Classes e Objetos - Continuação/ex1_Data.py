"""Crie uma classe para representar e manipular datas, com validação automática e
formatação.
### Atributos
- `dia` (inteiro): valor entre 1 e 31
- `mes` (inteiro): valor entre 1 e 12
- `ano` (inteiro): ano da data
### Métodos Obrigatórios
**`__init__(dia, mes, ano)`**
- Inicializa a data
- Valida se a data é válida (considerando bissexto)
- Levanta exceção se inválida
**`eh_bissexto()`**
- Retorna `True` se o ano é bissexto
- Retorna `False` caso contrário
- Regra: divisível por 4, exceto anos divisíveis por 100 (a menos que também sejam
por 400)
**`formatar()`**
- Retorna a data formatada como string: `DD/MM/AAAA`
- Exemplo: `31/12/2024`
**`avancar_dia()`**
- Avança a data em 1 dia
- Ao atingir o último dia do mês, avança para o primeiro dia do próximo
- Ao atingir 31 de dezembro, avança para 1o de janeiro do ano seguinte
- Considera meses com diferentes números de dias
- Considera anos bissextos"""

class Data:
    def __init__(self, dia, mes, ano):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        if not self._data_valida():
            raise ValueError("Data inválida")
    def eh_bissexto(self):
        return (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0)
    def _dias_no_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            return 29 if self.eh_bissexto() else 28
        else:
            return 0
    def _data_valida(self):
        if self.mes < 1 or self.mes > 12:
            return False
        if self.dia < 1 or self.dia > self._dias_no_mes():
            return False
        return True
    def formatar(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"
    def avancar_dia(self):
        self.dia += 1
        if self.dia > self._dias_no_mes():
            self.dia = 1
            self.mes += 1
            if self.mes > 12:
                self.mes = 1
                self.ano += 1
# Teste 1: Data válida comum
data = Data(15, 6, 2024)
print(data.formatar()) # Esperado: 15/06/2024
# Teste 2: Avançar dia simples
data = Data(15, 6, 2024)
data.avancar_dia()
print(data.formatar()) # Esperado: 16/06/2024
# Teste 3: Mudança de mês
data = Data(30, 6, 2024)
data.avancar_dia()
print(data.formatar()) # Esperado: 01/07/2024
# Teste 4: Mudança de ano
data = Data(31, 12, 2024)
data.avancar_dia()
print(data.formatar()) # Esperado: 01/01/2025
# Teste 5: Ano bissexto (29 de fevereiro)
data = Data(29, 2, 2024)
print(data.eh_bissexto()) # Esperado: True
# Teste 6: Ano não-bissexto (fevereiro tem 28 dias)
data = Data(28, 2, 2023)
data.avancar_dia()
print(data.formatar()) # Esperado: 01/03/2023