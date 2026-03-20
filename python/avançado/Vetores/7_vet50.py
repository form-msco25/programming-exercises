"""Construa um programa que:
a. Crie e armazene num vetor os 50 números (aleatoriamente ou por
introdução)
b. calcule a soma dos 50 números
c. Apresente no ecrã todos os números pares
d. Indique qual o menor número lido
e. Pesquisar um número no vetor (caso o número não seja encontrado
deve ser apresentada uma mensagem de erro: "numero não
encontrado".)"""

"""from random import randint

if __name__ == "__main__":

    vetor = [randint(0, 250) for x in range(50)]
    print("Vetor:", vetor)

    print(f"A soma dos valores é {sum(vetor)}.")

    vetor_pares = [i for i in vetor if i%2==0 and i!=0]
    print("Vetor com números pares:", vetor_pares)

    print("O menor número do vetor principal é:", min(vetor))

    if vetor_pares:
        print("O menor número par é:", min(vetor_pares))
    else:
        print("Não há números pares no vetor.")"""

from random import randint

if __name__=="__main__":

    vetor = []
    for x in range(50):
        num = randint(0, 250)
        vetor.append(num)        
    print("Vetor: ", vetor)
    print(f"A soma dos vetores é {sum(vetor)}.")
    vetor_pares = []
    for i in vetor:
        if (i%2==0 and i!=0):
            vetor_pares.append(i)
    print("Vetor com números pares: ", vetor_pares)
    vetor_ordenado = min(vetor)
    print("O menor número lido no vetor principal é ", vetor_ordenado)
    vetor_pares_ordenado = min(vetor_pares)
    print("O menor número lido no vetor par é ", vetor_pares_ordenado)

    cond = input("Deseja procurar um número? Responda S/N: ").lower()
    if cond=="s":
        cond=True
    else:
        cond=False
        print("Obrigado, volte sempre!")    
    while cond:        
        decision = int(input("1 para o vetor principal\n" 
                             "2 para o vetor pares\n"
                             "0 para sair do programa\n"))
        if decision==1:            
            procura = int(input("Digite o número que deseja procurar: "))
            if procura in vetor:
                print(f"Número {procura} encontrado no vetor principal.")
            else:
                print(f"Número {procura} não encontrado.")
            cond=False
        elif decision==2:            
            procura = int(input("Digite o número par que deseja procurar: "))
            if procura in vetor_pares:
                print(f"Número {procura} encontrado no vetor de pares.")
            else:
                print(f"Número {procura} não encontrado.")
            cond=False
        elif decision==0:
            print("Fim do programa.")
            cond=False                                    
        else:
            print("Entrada inválida.")