"""
### Descrição
Controle automático de temperatura de um ambiente.
### Atributos
- `temperatura_atual` (float): temperatura atual em °C
- `temperatura_desejada` (float): temperatura alvo
- `modo` (string): "manual" ou "auto"
- `ativo` (bool): se o sistema está ligado
### Métodos Obrigatórios
**`__init__(temp_atual, temp_desejada, modo="manual")`**
- Inicializa termostato
- Começa desligado
**`ligar()`**
- Liga o sistema
**`desligar()`**
- Desliga o sistema
**`aumentar_temperatura(graus)`**
- Aumenta temperatura_desejada
- Máximo 30°C
**`diminuir_temperatura(graus)`**
- Diminui temperatura_desejada
- Mínimo 10°C
**`regulacao_automatica()`**
- Se modo é "auto" e ativo:
- Se temp_atual < temp_desejada: aquece (+1°C)
- Se temp_atual > temp_desejada: esfria (-1°C)
- Se temp_atual = temp_desejada: mantém
**`status()`**
- Retorna string com estado completo:
- "Termostato desligado"
- "Aquecendo... (22°C / 25°C)"
- "Resfriando... (28°C / 24°C)"
- "Temperatura ideal! (25°C / 25°C)"
"""

class Termostato:
    def __init__(self, temp_atual, temp_desejada, modo="manual"):
        self.temperatura_atual = float(temp_atual)
        self.temperatura_desejada = float(temp_desejada)
        self.modo = modo.lower()
        self.ativo = False
    def ligar(self):
        self.ativo = True
    def desligar(self):
        self.ativo = False
    def aumentar_temperatura(self, graus):
        self.temperatura_desejada += graus
        if self.temperatura_desejada > 30:
            self.temperatura_desejada = 30
    def diminuir_temperatura(self, graus):
        self.temperatura_desejada -= graus
        if self.temperatura_desejada < 10:
            self.temperatura_desejada = 10
    def regulacao_automatica(self):
        if self.modo != "auto" or not self.ativo:
            return
        if self.temperatura_atual < self.temperatura_desejada:
            self.temperatura_atual += 1
        elif self.temperatura_atual > self.temperatura_desejada:
            self.temperatura_atual -= 1
    def status(self):
        if not self.ativo:
            return "Termostato desligado"
        if self.temperatura_atual < self.temperatura_desejada:
            return f"Aquecendo... ({self.temperatura_atual:.1f}°C / {self.temperatura_desejada:.1f}°C)"
        elif self.temperatura_atual > self.temperatura_desejada:
            return f"Resfriando... ({self.temperatura_atual:.1f}°C / {self.temperatura_desejada:.1f}°C)"
        else:
            return f"Temperatura ideal! ({self.temperatura_atual:.1f}°C / {self.temperatura_desejada:.1f}°C)"
# Teste 1: Criar e ligar termostato
termo = Termostato(20, 25, "auto")
termo.ligar()
termo.regulacao_automatica()
print(termo.temperatura_atual) # Esperado: 21 (aquecimento)
# Teste 2: Regulação contínua
for i in range(5):
    termo.regulacao_automatica()
    print(termo.temperatura_atual) # Esperado: 25 (atingiu meta)
# Teste 3: Controle manual
termo = Termostato(22, 22, "manual")
termo.ligar()
termo.aumentar_temperatura(2)
print(termo.temperatura_desejada) # Esperado: 24
# Teste 4: Status detalhado
termo = Termostato(22, 25, "auto")
termo.ligar()
print(termo.status()) # Esperado: "Aquecendo... (22°C / 25°C)"
# Teste 5: Limite máximo/mínimo
termo.aumentar_temperatura(10) # Tenta 25 + 10 = 35
print(termo.temperatura_desejada) # Esperado: 30 (máximo)
termo.diminuir_temperatura(25) # Tenta 30 - 25 = 5
print(termo.temperatura_desejada) # Esperado: 10 (mínimo)