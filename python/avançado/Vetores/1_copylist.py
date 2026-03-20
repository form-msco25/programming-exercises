"""Criar um array A com 5 elementos inteiro. Construir um vetor B do mesmo tipo
e tamanho e com os “mesmo” elementos do vetor A."""

if __name__=="__main__":
    array_a = []
    for i in range(5):
        num = int(input("Digite 5 números inteiros: "))
        array_a.append(num)
    print(f"Vetor A: {array_a}")
    array_b = array_a.copy()
    print(f"Vetor B: {array_b}")