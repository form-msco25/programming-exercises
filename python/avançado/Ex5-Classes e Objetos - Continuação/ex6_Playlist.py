"""
### Descrição
Gerencie uma playlist musical com adição/remoção de músicas e cálculo de
duração.
### Atributos
- `nome` (string): nome da playlist
- `musicas` (lista): lista de dicionários com {'titulo': str, 'duracao_segundos': int}
### Métodos Obrigatórios
**`__init__(nome)`**
- Inicializa playlist vazia
**`adicionar_musica(titulo, duracao_segundos)`**
- Adiciona nova música à playlist
- Valida se duração é positiva
- Evita músicas duplicadas (mesmo título)
**`remover_musica(titulo)`**
- Remove música pelo título
- Retorna True se removida, False se não encontrada
**`duracao_total()`**
- Calcula duração total da playlist
- Retorna string formatada: "45:32" (minutos:segundos)
**`tocar_aleatoria()`**
- Seleciona e retorna uma música aleatória
- Retorna dicionário com a música
**`listar_musicas()`**
- Imprime todas as músicas com números
- Formato: "1. Bohemian Rhapsody (5:55)"
"""

import random

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []
    def adicionar_musica(self, titulo, duracao_segundos):
        if duracao_segundos <= 0:
            raise ValueError("A duração deve ser positiva.")
        for musica in self.musicas:
            if musica['titulo'].lower() == titulo.lower():
                print("Música já existe na playlist.")
                return
        self.musicas.append({
            'titulo': titulo,
            'duracao_segundos': duracao_segundos
        })
    def remover_musica(self, titulo):
        for musica in self.musicas:
            if musica['titulo'].lower() == titulo.lower():
                self.musicas.remove(musica)
                return True
        return False
    def duracao_total(self):
        total_segundos = sum(m['duracao_segundos'] for m in self.musicas)
        minutos = total_segundos // 60
        segundos = total_segundos % 60
        return f"{minutos}:{segundos:02d}"
    def tocar_aleatoria(self):
        if not self.musicas:
            return None
        return random.choice(self.musicas)
    def listar_musicas(self):
        if not self.musicas:
            print("Playlist vazia.")
            return
        for i, musica in enumerate(self.musicas, start=1):
            minutos = musica['duracao_segundos'] // 60
            segundos = musica['duracao_segundos'] % 60
            print(f"{i}. {musica['titulo']} ({minutos}:{segundos:02d})")
# Teste 1: Criar playlist e adicionar músicas
pl = Playlist("Rock Clássico")
pl.adicionar_musica("Bohemian Rhapsody", 355) # 5:55
pl.adicionar_musica("Stairway to Heaven", 482) # 8:02
pl.adicionar_musica("Hotel California", 391) # 6:31
# Teste 2: Duração total
print(pl.duracao_total()) # Esperado: "23:28"
# Teste 3: Listar músicas
pl.listar_musicas() # Exibe: 1. Bohemian Rhapsody (5:55) etc
# Teste 4: Remover música
pl.remover_musica("Stairway to Heaven")
print(pl.duracao_total()) # Esperado: "12:26"
# Teste 5: Música aleatória
musica = pl.tocar_aleatoria()
print(musica['titulo']) # Uma das músicas restantes
# Teste 6: Evitar duplicatas
pl.adicionar_musica("Bohemian Rhapsody", 300) # Não adiciona
print(len(pl.musicas)) # Esperado: 2