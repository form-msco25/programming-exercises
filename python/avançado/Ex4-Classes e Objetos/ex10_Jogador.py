"""Crie uma classe `Jogador` com os seguintes atributos:
- `nome` (string)
- `vida` (inteiro, começando em 100)
- `energia` (inteiro, começando em 100)
Implemente os seguintes métodos:
- `atacar(outro_jogador, dano=10)`: reduz a vida do outro jogador em `dano`
unidades
- `usar_energia(quantidade)`: reduz a energia em `quantidade` unidades (não pode
ser negativa)
- `recuperar_energia(quantidade)`: aumenta a energia em `quantidade` unidades
- `exibir_status()`: imprime nome, vida e energia atuais
- `verificar_derrota()`: retorna True se vida ≤ 0
**Teste:** Crie dois jogadores, façam ataques mútuos, recuperem energia e
verifique o status final."""

class Jogador:
    def __init__(self, nome, vida=100, energia=100):
        self.nome = nome
        self.vida = vida
        self.energia = energia

    def atacar(self, outro_jogador, dano=10):
        outro_jogador.vida -= dano

    def usar_energia(self, quantidade):
        if quantidade > self.energia:
            print("Energia insuficiente")
        else:
            self.energia -= quantidade

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100

    def exibir_status(self):
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Energia: {self.energia}")

    def verificar_derrota(self):
        return self.vida <= 0
            
player1 = Jogador("Michael")
player2 = Jogador("Steven")

player1.atacar(player2)
player2.atacar(player1)

player1.usar_energia(94)
player2.usar_energia(99)

player1.recuperar_energia(50)
player2.recuperar_energia(57)

player1.exibir_status()
player2.exibir_status()

if player1.verificar_derrota():
    print(f"Jogador {player2.nome} WINS!!!")
elif player2.verificar_derrota():
    print(f"Jogador {player1.nome} WINS!!!")
else:
    print("Nenhum jogador foi derrotado.")