"""Converta uma string de e-mail para set de caracteres únicos, verifique
com in se contém "@" e conte vogais únicas."""
email = input("Introduza o e-mail: ").lower()
set_email = set(email)
print(f"Caracteres únicos do e-mail: {set_email}")
if "@" in set_email:
    print("O e-mail contém '@'")
else:
    print("O e-mail não contém '@'")
vogais = {"a", "e", "i", "o", "u"}
vogais_unicas = set_email & vogais
print(f"Vogais únicas no e-mail: {vogais_unicas}")
print(f"Total de vogais únicas: {len(vogais_unicas)}")