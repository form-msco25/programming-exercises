"""Considere o seguinte código:
def announce(f):
def wrapper():
print("Sobre o correr a função ...")
f()
print("Está feito a função.")
return wrapper
@announce
def ola():
print("Olá Mundo!")
ola()
Tarefa: Escreva em comentários, linha a linha, o que acontece quando o Python executa
ola(). Identifique em que momento a função announce é chamada e o que é exatamente
wrapper."""

# Define o decorator 'announce' que recebe uma função 'f' como argumento
def announce(f):
    # Dentro de announce, é definida a função 'wrapper' que envolve a função original
    def wrapper():
        # Esta linha será executada quando 'wrapper()' for chamado
        print("Sobre o correr a função ...")
        # É chamada a função original passada como argumento 'f'
        f()
        # Esta linha também será executada dentro do wrapper
        print("Está feito a função.")
    # Retorna a função 'wrapper' (não executa ainda, apenas retorna a referência)
    return wrapper
# Aplica o decorator 'announce' à função 'ola'
@announce
def ola():
    print("Olá Mundo!")
# Nesse ponto, 'ola' deixa de ser a função original, passando a ser a função 'wrapper'
# que foi retornada pelo decorator. É como se tivesse sido feito:
# ola = announce(ola)
# Chama a função 'ola' (que agora é 'wrapper')
ola()
