"""Escreva um programa que receba três notas de um aluno (tipo float) e calcule a média. Com base na média, exiba o resultado:
"Reprovado" 7
"Recuperação" mais do que 7 e menos do que 9.5
"Aprovado" 9.5 até 12
"Aprovado com mérito" 12 a 17
"Aprovado com excelência"  17 a 20"""

if __name__ == "__main__":

    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))

    media = (nota1 + nota2 + nota3)/3
    print(f"A média das notas é: {media}")

    if media <= 7:
        print("Reprovado")
    elif media > 7 and media < 9.5:
        print("Recuperação")
    elif media >= 9.5 and media < 12:
        print("Aprovado")
    elif media >= 12 and media < 17:
        print("Aprovado")
    elif media >= 17 and media <= 20:
        print("Aprovado com excelência")
    else:
        print("As notas que foram inseridas são inválidas.")