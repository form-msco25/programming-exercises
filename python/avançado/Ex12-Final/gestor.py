from jogador import Jogador
import pandas as pd
from functools import wraps

# Lista para armazenar jogadores
jogadores = []

# Decorador para registar ações
def registar_acao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Ação executada: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@registar_acao
def adicionar_jogador(nome, idade, posicao, golos):
    jogador = Jogador(nome, idade, posicao, golos)
    jogadores.append(jogador)
@registar_acao
def listar_jogadores():
    print("\nLista de Jogadores:")
    for j in jogadores:
        print(j)
@registar_acao
def estatisticas_equipa():
    # Criar DataFrame com Pandas
    data = {
        "Nome": [j.nome for j in jogadores],
        "Idade": [j.idade for j in jogadores],
        "Posição": [j.posicao for j in jogadores],
        "Golos": [j.golos for j in jogadores]
    }
    df = pd.DataFrame(data)
    print("\nEstatísticas da Equipa:")
    print(df.describe(include='all'))
    return df