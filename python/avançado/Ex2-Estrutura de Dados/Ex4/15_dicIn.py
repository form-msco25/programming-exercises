"""Dado um dicionário que mapeia códigos de país para nomes (por exemplo, 'PT':
'Portugal'), verifique se um certo código está presente usando in."""

paises = {"PT":"Portugal", "ESP" : "España", "ECU" : "Ecuador", "JPN" : "Japan"}
prefixo = input("Introduza o prefixo do país que deseja verificar: ").upper()
if prefixo in paises:
    print(f"O prefixo '{prefixo}' corresponde a '{paises.get(prefixo)}'")
else:
    print(f"O prefixo '{prefixo}' não consta no conjunto de países.")