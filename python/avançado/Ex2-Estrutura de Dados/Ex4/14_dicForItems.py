"""Usando um dicionário, percorra todos os pares chave:valor com um ciclo for e
imprima-os formatados."""

dicionario = {"honda v" : "civic", "honda b" : "cb125r", "smart" : "fortwo", "volvo" : "s40"}
print("Garagem: ")
for marca, modelo in dicionario.items():
    print(f"{marca} - {modelo}")