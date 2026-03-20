"""Criar um vetor A com 8 elementos inteiros. Construir um vetor B do mesmo
tipo e tamanho e com os elementos do vetor A multiplicados por 2."""

if __name__=="__main__":
    array_a = []
    for i in range(8):
        num = int(input("Digite 8 números inteiros: "))
        array_a.append(num)
    print(f"Vetor A: {array_a}")
    array_b = array_a.copy()
    for i in range(len(array_b)):
        array_b[i] = array_b[i] * 2
    print(f"Vetor B: {array_b}")
    