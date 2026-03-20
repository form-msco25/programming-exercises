"""Crie um tuplo de palavras de uma senha; converta para set, remova
vogais e verifique se a senha original tem pelo menos 3 consoantes
únicas com in."""
senha = ("Segura", "123", "Exemplo")
caracteres_unicos = set("".join(senha).lower())
print(f"Caracteres únicos da senha: {caracteres_unicos}")
vogais = {"a", "e", "i", "o", "u"}
consoantes = {c for c in caracteres_unicos if c.isalpha() and c not in vogais}
print(f"Consoantes únicas da senha: {consoantes}")
if len(consoantes) >= 3:
    print("A senha tem pelo menos 3 consoantes únicas.")
else:
    print("A senha não tem pelo menos 3 consoantes únicas.")
consoante_unica = "s"
if consoante_unica in consoantes:
    print(f"A consoante '{consoante_unica}' está presente na senha.")