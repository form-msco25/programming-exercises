"""Crie uma matriz 5x5 inicializada com zeros e exiba-a no formato de matriz."""

if __name__=="__main__":
    
    matriz = [[0 for j in range(5)] for i in range(5)]
    print("Matriz: ")
    for linha in matriz:
        print(linha)