"""Adapte o decorator announce para que funcione com funções que possuem parâmetros.
Utilize *args e **kwargs na função wrapper.
Crie uma função cumprimentar(nome) que imprime "Olá, {nome}!" e decore-a com o
decorator adaptado. Teste chamando cumprimentar("Ana")."""

def announce(f):
    def wrapper(*args, **kwargs):
        print("[INFO] Iniciando execução da função...")
        f(*args, **kwargs)
        print("[INFO] Execução concluída com sucesso!")
    return wrapper
@announce
def cumprimentar(nome):
    print(f"Olá, {nome}!")
cumprimentar("Ana")
