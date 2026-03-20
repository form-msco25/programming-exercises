"""Criar um vetor A com 10 elementos inteiros. Construir um vetor B do mesmo
tipo e tamanho, sendo que cada elemento do vetor B deverá ser o respetivo
elemento de A multiplicado pela sua posição."""

if __name__=="__main__":

    vetor_a = []
    vetor_b = []

    for i in range(10):
        num = int(input("Digite um número inteiro: "))
        vetor_a.append(num)
        print("Vetor A: ", vetor_a)
        vetor_b.append(num*i)
        print("Vetor B: ", vetor_b)