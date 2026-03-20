"""Faça um dicionário de dados sobre automóveis. Exemplo: Marca “BMW”,
Modelo “i3”. Realize as seguintes operações:
a. Crie um dicionário com pelo menos 5 marcas de automóveis e os
respetivos modelos.
b. Liste o dicionário.
c. Crie um novo elemento ao dicionário para
uma mesma marca.
d. Volte a listar."""

stand = {"honda-auto":["civic"], "honda-moto":["cb125r"], "smart":["fortwo"], "volvo":["s40"], "nissan":["gtr"]}
for marca, modelo in stand.items():
    print(f"Marca: {marca} - Modelo: {modelo}")
entrada = input("Deseja introduzir um novo modelo para uma marca já existente? Digite s/n: ").lower()
if entrada=="s":
    marca_existente = input("Coloque a marca do modelo que deseja adicionar: ").lower()
    if marca_existente in stand:
        novo_modelo = input("Introduza o modelo: ").lower()
        stand[marca_existente].append(novo_modelo)
    else:
        print(f"A {marca_existente} não consta no inventário.")
elif entrada.isalpha()==False:
    print("Entrada inválida.")
else:
    print("Obrigado. Até breve!")
print("---INVENTÁRIO ATUALIZADO---")
for marca, modelo in stand.items():
    print(f"Marca: {marca} - Modelo: {modelo}")