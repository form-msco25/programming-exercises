"""Crie um tuplo com os dias da semana e mostre no ecrã apenas o primeiro e o
último elemento."""

semana = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta--feira", "sábado", "domingo")
print(f"Sendo que o primeiro dia da semana é '{semana[0]}' e o último é '{semana[6]}'.")
num = int(input("Digite o número do dia da semana que deseja ver: "))
print(f"Dia da semana: {semana[num-1]}")