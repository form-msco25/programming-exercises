"""Modifique o decorator announce para mostrar mensagens mais descritivas:
• Antes: "[INFO] Iniciando execução da função..."
• Depois: "[INFO] Execução concluída com sucesso!"
Teste com a função ola() decorada."""
def announce(f):
    def wrapper():
        print("[INFO] Iniciando execução da função...")
        f()
        print("[INFO] Execução concluída com sucesso!")
    return wrapper
@announce
def ola():
    print("Olá Mundo!")
ola()
