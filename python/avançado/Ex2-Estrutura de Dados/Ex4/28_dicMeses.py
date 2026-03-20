"""Crie um dicionário que mapeia meses (1 a 12) para o número de dias. Peça um
número de mês ao utilizador e apresente o total de dias."""
""""janeiro":31, "fevereiro":28, "março":31, "abril": 30, "maio":31, "junho": 30, "julho": 31, 
         "agosto":31, "setembro":30, "outubro":31, "novembro":30, "dezembro":31"""
meses = {}
for i in range(1, 13):    
    if i%2!=0 and i<=7:
        meses[i]=31
    elif i%2==0 and i>7:
        meses[i]=31
    elif i==2:
        meses[i]=28
    else:
        meses[i]=30
mes = int(input("Digite o número do mês que deseja verificar: "))
print(f"O mês número {mes} tem {meses.get(mes)}.")
print(meses)
