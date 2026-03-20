"""Leia valores do utilizador e preencha uma matriz 3x3. Exiba a matriz no final."""

if __name__=="__main__":
    
    matriz = [[int(input(f"Digite um valor para a posição [{i}][{j}]: ")) for j in range(3)]for i in range(3)]
    print("Matriz: ") 
    for linha in matriz:
        print(linha)