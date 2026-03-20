POSICOES = ("Guarda-redes", "Defesa", "Médio", "Avançado")
POSICOES_SET = set(POSICOES)

def validar_posicao(posicao):
    return posicao in POSICOES_SET