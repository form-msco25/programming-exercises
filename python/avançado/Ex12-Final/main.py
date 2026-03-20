import tkinter as tk
from tkinter import messagebox
from gestor import adicionar_jogador, listar_jogadores, estatisticas_equipa
from utils import validar_posicao, POSICOES
# Função para adicionar jogador via interface
def registar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    posicao = entry_posicao.get()
    golos = entry_golos.get()
    if not validar_posicao(posicao):
        messagebox.showerror("Erro", f"Posição inválida! Escolha: {', '.join(POSICOES)}")
        return
    try:
        idade = int(idade)
        golos = int(golos)
    except ValueError:
        messagebox.showerror("Erro", "Idade e golos devem ser números inteiros!")
        return
    adicionar_jogador(nome, idade, posicao, golos)
    messagebox.showinfo("Sucesso", f"Jogador {nome} registado com sucesso!")
# Interface Tkinter
root = tk.Tk()
root.title("Gestor de Equipa de Futebol")
tk.Label(root, text="Nome:").grid(row=0, column=0)
tk.Label(root, text="Idade:").grid(row=1, column=0)
tk.Label(root, text="Posição:").grid(row=2, column=0)
tk.Label(root, text="Golos:").grid(row=3, column=0)
entry_nome = tk.Entry(root)
entry_idade = tk.Entry(root)
entry_posicao = tk.Entry(root)
entry_golos = tk.Entry(root)
entry_nome.grid(row=0, column=1)
entry_idade.grid(row=1, column=1)
entry_posicao.grid(row=2, column=1)
entry_golos.grid(row=3, column=1)
tk.Button(root, text="Registar Jogador", command=registar).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Listar Jogadores", command=listar_jogadores).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Estatísticas da Equipa", command=estatisticas_equipa).grid(row=6, column=0, columnspan=2)
root.mainloop()