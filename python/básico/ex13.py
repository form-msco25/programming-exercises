"""Descrição: 
Escreva um programa que peça ao utilizador para introduzir um número entre 1 e 10.
O programa deve continuar a pedir o número enquanto o utilizador não introduzir um valor válido.  

Requisitos:  
Use um ciclo while.
Valide se o número está entre 1 e 10. 
Imprima uma mensagem de erro para entradas inválidas.

Exemplo de interação esperada:      
Introduza um número entre 1 e 10: 15 
Número inválido. Tente novamente. 
Introduza um número entre 1 e 10: -3 
Número inválido. Tente novamente. 
Introduza um número entre 1 e 10: 7 
Obrigado! Número válido: 7"""

if __name__ == "__main__":
    
    """var = True    
    while var:
        n = int(input("Digite um número entre 1 e 10: "))
        if n>=1 and n<=10:
            print(f"Obrigado! Número válido: {n}")            
            var = False
        else:
            print("Número inválido. Tente novamente.")"""    
    
    var = True
    while var:
        n = int(input("Digite um número entre 1 e 10: "))
        if n<1 or n>10:
            print("Número inválido. Tente novamente.")
            continue
        print(f"Obrigado! Número válido: {n}")
        var = False
        
            
        
        
