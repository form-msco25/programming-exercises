"""Crie um pequeno sistema de login com um dicionário que guarda utilizadores e
palavras-passe. Leia um utilizador e palavra-passe e verifique se a combinação
está correta usando in e comparação de valores."""

contas = {}
for i in range(5):
    user = input("Introduza o seu username: ").lower()
    password = input("Digite a sua palavra-passe: ").lower()
    contas[user] = password
print("=====LOGIN=====")
user_log = input("Digite o seu username: ").lower()
if user_log in contas.keys():
    palavra_passe = input("Digite a sua palavra-passe: ").lower()
    if palavra_passe == contas[user_log]:
        print("Login efetuado com sucesso!")
    else:
        print("Palavra-passe errada.")
else:
    print("Utilizador inexistente.")