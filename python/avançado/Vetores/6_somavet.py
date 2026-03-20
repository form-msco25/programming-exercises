"""Criar dois vetores A e B cada um com 10 elementos inteiros. Construir um vetor
C, onde cada elemento de C é a soma dos respetivos elementos de A e B."""

if __name__=="__main__":

    vetor_a = []
    vetor_b = []
    vetor_c = []

    for i in range(10):
        num_a = int(input("Digite um número inteiro para o vetor A: "))
        vetor_a.append(num_a)
        print("Vetor A: ", vetor_a)        
        num_b = int(input("Digite um número inteiro para o vetor B: "))
        vetor_b.append(num_b)
        print("Vetor B: ", vetor_b)
        vetor_c.append(num_a + num_b)
        print("A soma dos vetores: ", vetor_c)
