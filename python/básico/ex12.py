"""Descrição:
Escreva um programa que utilize um ciclo while para imprimir todos os números de 1 a 5.  

Requisitos:  
  Use um ciclo while.  
  Comece a contagem a partir de 1 e termine em 5.
Exemplo de saída esperada:    
Número: 1

Número: 2

Número: 3

Número: 4

Número: 5"""

if __name__ == "__main__":
    i = 0
    while i<5:
        i+=1
        print(f"Número: {i}")