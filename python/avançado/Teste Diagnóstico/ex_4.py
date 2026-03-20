"""Escreva um programa que solicite ao utilizador que escreva um número e, em
seguida, imprima a tabuada desse número. Utilize a instrução “While”."""

if __name__=="__main__":    
    num = int(input("Digite um número: "))    
    i=0
    while i<=10:
        res = num * i
        print(res)
        i += 1
