class Jogador:
    def __init__(self, nome, idade, posicao, golos):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.golos = golos
    def __str__(self):
        return f"{self.nome} | {self.idade} anos | {self.posicao} | {self.golos} golos"