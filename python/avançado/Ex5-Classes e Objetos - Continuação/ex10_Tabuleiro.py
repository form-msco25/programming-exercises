"""### Descrição
Implemente um tabuleiro básico para jogo de damas 8x8.
### Atributos
- `tamanho` (int): 8 (8x8)
- `tabuleiro` (list): matriz 8x8 representando o jogo
- `pecas_brancas` (int): número de peças brancas
- `pecas_pretas` (int): número de peças pretas
### Representação
- 'B' = peça branca
- 'P' = peça preta
- ' ' = espaço vazio
### Métodos Obrigatórios
**`__init__()`**
- Inicializa tabuleiro 8x8
- Posiciona 12 peças brancas nas 3 primeiras linhas
- Posiciona 12 peças pretas nas 3 últimas linhas
- Linhas pares começam em coluna 1 (para efeito de xadrez)
**`exibir_tabuleiro()`**
- Imprime tabuleiro formatado
- Mostra linhas (0-7) e colunas (A-H)
- Usa grid visual
**`mover_peca(cor, linha_origem, col_origem, linha_dest, col_dest)`**
- Move peça de uma posição para outra
- Valida se movimento é diagonal
- Valida se destino está vazio
- Retorna True se sucesso, False se falhou
**`capturar_peca(linha_origem, col_origem, linha_dest, col_dest)`**
- Remove peça adversária se houver entre origem e destino
- Valida captura válida
- Reduz contador de peças
**`verificar_vitoria()`**
- Retorna 'brancas' se pretas = 0
- Retorna 'pretas' se brancas = 0
- Retorna None se jogo continua
**`listar_movimentos_possiveis(cor, linha, coluna)`**
- Retorna lista de movimentos válidos para uma peça"""

class Tabuleiro:
    def __init__(self):
        self.tamanho = 8
        self.tabuleiro = [[' ' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.pecas_brancas = 12
        self.pecas_pretas = 12
        self._inicializar_tabuleiro()
    def _inicializar_tabuleiro(self):
        # Posicionar peças brancas nas 3 primeiras linhas
        for linha in range(3):
            for coluna in range(self.tamanho):
                if (linha + coluna) % 2 != 0:  # posições alternadas tipo xadrez
                    self.tabuleiro[linha][coluna] = 'B'
        # Posicionar peças pretas nas 3 últimas linhas
        for linha in range(5, 8):
            for coluna in range(self.tamanho):
                if (linha + coluna) % 2 != 0:
                    self.tabuleiro[linha][coluna] = 'P'
    def exibir_tabuleiro(self):
        print("   A   B   C   D   E   F   G   H")
        print("  +" + "---+"*self.tamanho)
        for i, linha in enumerate(self.tabuleiro):
            linha_str = f"{i} | " + " | ".join(linha) + " |"
            print(linha_str)
            print("  +" + "---+"*self.tamanho)
    def mover_peca(self, cor, linha_origem, col_origem, linha_dest, col_dest):
        # Verificar se há peça na origem e se é da cor correta
        if self.tabuleiro[linha_origem][col_origem] != cor:
            return False
        # Verificar se destino está vazio
        if self.tabuleiro[linha_dest][col_dest] != ' ':
            return False
        # Verificar movimento diagonal (diferença absoluta de linhas e colunas igual)
        if abs(linha_dest - linha_origem) != abs(col_dest - col_origem):
            return False
        # Movimento simples (uma casa)
        if abs(linha_dest - linha_origem) == 1:
            self.tabuleiro[linha_dest][col_dest] = cor
            self.tabuleiro[linha_origem][col_origem] = ' '
            return True
        # Movimento de captura (duas casas)
        elif abs(linha_dest - linha_origem) == 2:
            return self.capturar_peca(linha_origem, col_origem, linha_dest, col_dest)
        else:
            return False
    def capturar_peca(self, linha_origem, col_origem, linha_dest, col_dest):
        # Calcular posição da peça que será capturada
        linha_meio = (linha_origem + linha_dest) // 2
        col_meio = (col_origem + col_dest) // 2
        peca_meio = self.tabuleiro[linha_meio][col_meio]
        cor_origem = self.tabuleiro[linha_origem][col_origem]
        if cor_origem == 'B' and peca_meio == 'P':
            self.pecas_pretas -= 1
        elif cor_origem == 'P' and peca_meio == 'B':
            self.pecas_brancas -= 1
        else:
            return False  # não há peça adversária para capturar
        # Executar captura
        self.tabuleiro[linha_dest][col_dest] = cor_origem
        self.tabuleiro[linha_origem][col_origem] = ' '
        self.tabuleiro[linha_meio][col_meio] = ' '
        return True
    def verificar_vitoria(self):
        if self.pecas_pretas == 0:
            return 'brancas'
        elif self.pecas_brancas == 0:
            return 'pretas'
        else:
            return None
    def listar_movimentos_possiveis(self, cor, linha, coluna):
        movimentos = []
        direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for d_linha, d_col in direcoes:
            nova_linha = linha + d_linha
            nova_col = coluna + d_col
            # Movimento simples dentro do tabuleiro
            if 0 <= nova_linha < self.tamanho and 0 <= nova_col < self.tamanho:
                if self.tabuleiro[nova_linha][nova_col] == ' ':
                    movimentos.append((nova_linha, nova_col))
            # Movimento de captura
            capt_linha = linha + 2*d_linha
            capt_col = coluna + 2*d_col
            if 0 <= capt_linha < self.tamanho and 0 <= capt_col < self.tamanho:
                meio_peca = self.tabuleiro[linha + d_linha][coluna + d_col]
                if self.tabuleiro[capt_linha][capt_col] == ' ':
                    if cor == 'B' and meio_peca == 'P':
                        movimentos.append((capt_linha, capt_col))
                    elif cor == 'P' and meio_peca == 'B':
                        movimentos.append((capt_linha, capt_col))
        return movimentos
# Teste 1: Criar tabuleiro
tab = Tabuleiro()
print(f"Brancas: {tab.pecas_brancas}, Pretas: {tab.pecas_pretas}")
# Esperado: Brancas: 12, Pretas: 12
# Teste 2: Exibir tabuleiro
tab.exibir_tabuleiro()
# Teste 3: Mover peça
resultado = tab.mover_peca('B', 2, 1, 3, 2)
print(resultado) # Esperado: True
# Teste 4: Movimento inválido (não-diagonal)
resultado = tab.mover_peca('B', 3, 2, 3, 4)
print(resultado) # Esperado: False
# Teste 5: Capturar peça
# (Configurar tabuleiro para teste de captura)
tab.tabuleiro[4][3] = 'P' # Coloca peça preta
resultado = tab.capturar_peca('B', 3, 2, 5, 4)
print(resultado) # Esperado: True
# Teste 6: Verificar vitória
tab.pecas_pretas = 0
print(tab.verificar_vitoria()) # Esperado: 'brancas'