"""Crie um set a partir de uma string (por exemplo, 'banana') e analise quais
caracteres únicos existem."""

palavra = "ananâs"
print(f"A palavra é: {palavra}")
caracteres = list(palavra)
print(f"Separada por caracteres: {caracteres}")
set_caracteres = set(caracteres)
print(f"Sem letras repetidas: {set_caracteres}")