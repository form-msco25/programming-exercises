"""Criar um vetor A com 15 elementos inteiros. Construir um vetor B do mesmo
tipo e tamanho, sendo que cada elemento do vetor B deverá ser a raiz
quadrada do respetivo elemento de A."""

if __name__=="__main__":
    
    vetor_a = []
    vetor_b = []

    for i in range(15):
        num = int(input("Digite um número inteiro: "))
        vetor_a.append(num)
        print("Vetor A: ", vetor_a)
        vetor_b.append(num**0.5)
        print("Vetor B: ", vetor_b)