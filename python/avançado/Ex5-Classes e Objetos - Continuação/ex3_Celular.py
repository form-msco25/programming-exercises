"""
### Descrição
Simule um celular com controle de bateria e gerenciamento de chamadas.
### Atributos
- `modelo` (string): modelo do celular (ex: "iPhone 15")
- `bateria` (inteiro 0-100): percentual de bateria
- `em_chamada` (booleano): True se em chamada, False caso contrário
- `duracao_chamada` (inteiro): duração em segundos da chamada atual
### Métodos Obrigatórios
**`__init__(modelo, bateria_inicial)`**
- Inicializa o celular
- Define bateria inicial (máximo 100)
- Começa sem chamada ativa
**`fazer_chamada(duracao_minutos)`**
- Inicia uma chamada
- Consome 5% de bateria por minuto
- Define `em_chamada = True`
- Se bateria insuficiente, não inicia a chamada
**`encerrar_chamada()`**
- Encerra chamada em curso
- Define `em_chamada = False`
- Define duração para 0
**`carregar_bateria(percentual_adicional)`**
- Aumenta bateria do celular
- Máximo é 100%
**`status()`**
- Retorna string com todas as informações atuais
- Formato: "Modelo: iPhone 15 | Bateria: 85% | Em chamada: Não"
"""
class Celular:
    def __init__(self, modelo, bateria_inicial):
        self.modelo = modelo
        self.bateria = max(0, min(100, bateria_inicial))
        self.em_chamada = False
        self.duracao_chamada = 0
    def fazer_chamada(self, duracao_minutos):
        if self.em_chamada:
            print("Já existe uma chamada em andamento.")
            return
        consumo = duracao_minutos * 5
        if self.bateria < consumo:
            print("Bateria insuficiente para iniciar a chamada.")
            return
        self.bateria -= consumo
        self.em_chamada = True
        self.duracao_chamada = duracao_minutos * 60
    def encerrar_chamada(self):
        if not self.em_chamada:
            print("Não há chamada em andamento.")
            return
        self.em_chamada = False
        self.duracao_chamada = 0
    def carregar_bateria(self, percentual_adicional):
        if percentual_adicional < 0:
            print("Valor inválido para carregamento.")
            return
        self.bateria += percentual_adicional
        if self.bateria > 100:
            self.bateria = 100
    def status(self):
        chamada_str = "Sim" if self.em_chamada else "Não"
        return f"Modelo: {self.modelo} | Bateria: {self.bateria}% | Em chamada: {chamada_str}"
# Teste 1: Criar celular e fazer chamada
cel = Celular("iPhone 15", 100)
cel.fazer_chamada(10) # 10 minutos = 50% consumo
print(cel.bateria) # Esperado: 50
print(cel.em_chamada) # Esperado: True
# Teste 2: Encerrar chamada
cel.encerrar_chamada()
print(cel.em_chamada) # Esperado: False
print(cel.bateria) # Esperado: 50 (não muda ao encerrar)
# Teste 3: Carregar bateria
cel.carregar_bateria(40)
print(cel.bateria) # Esperado: 90 (50 + 40)
# Teste 4: Bateria máxima 100
cel.carregar_bateria(20)
print(cel.bateria) # Esperado: 100 (não ultrapassa 100)
# Teste 5: Bateria insuficiente
cel = Celular("Samsung", 30)
cel.fazer_chamada(10) # Precisaria 50%, mas tem só 30%
print(cel.em_chamada) # Esperado: False (não inicia)
# Teste 6: Status completo
cel = Celular("Pixel 8", 75)
print(cel.status()) # Esperado: "Modelo: Pixel 8 | Bateria: 75% | Em chamada: Não"