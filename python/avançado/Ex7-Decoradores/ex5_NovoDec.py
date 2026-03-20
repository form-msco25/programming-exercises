"""Crie um novo decorator chamado @maiusculas que:
1. Chame a função decorada
2. Se a função retornar uma string, converta-a para maiúsculas
3. Imprima o resultado em maiúsculas
Teste com uma função mensagem() que retorna uma string e aplique o decorator.
Dica:
Duas instruções dentro de def wrapper(*args, **kwargs):
resultado = f(*args, **kwargs) # Chama a função e guarda o resultado
if isinstance(resultado, str): # Verifica se é uma string"""

def maiusculas(f):
    def wrapper(*args, **kwargs):
        resultado = f(*args, **kwargs)
        if isinstance(resultado, str):
            resultado = resultado.upper()
        print(resultado)
    return wrapper
@maiusculas
def mensagem():
    return "Esta é uma mensagem especial."
mensagem()