"""Crie uma nova função despedida() que imprime "Até já!" e decore-a com o decorator
@announce. Execute ambas as funções e observe a saída.
Tarefa: Reutilize o decorator da Solução 1 para a nova função e demonstre que o mesmo
decorator funciona com diferentes funções."""

def announce(f):
    def wrapper():
        print("Sobre o correr a função ...")
        f()
        print("Está feito a função.")
    return wrapper
@announce
def ola():
    print("Olá Mundo!")
def despedida():
    print("Até já!")
ola()
despedida()