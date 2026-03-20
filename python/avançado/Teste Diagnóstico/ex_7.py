"""Crie uma função que se chame “CalcularPromocao” e que retorne um float,
dado o salário a função deve retornar o valor do salário + 10% se o salário for
inferior a 700 euros, caso seja igual ou superior a 700 euros deve adicionar 5%
apenas."""

def calcular_promocao():    
    if (salario < 700):
        promocao = salario * 0.1
        transferencia = salario + promocao
    else:
        promocao = salario * 0.05
        transferencia = salario + promocao
    print("Irá receber na sua conta bancária: %.2f.\nCom uma promoção de: %.2f" % (transferencia, promocao))

if __name__=="__main__":
    salario = float(input("Introduza o seu salário: "))
    calcular_promocao()