"""Crie um dicionário com três contactos (nome -> telefone). Adicione um novo
contacto e remova outro."""

contactos = {"michael" : 123456789, "steven" : 987654321, "afonso" : 999888777, "carlos" : 111222333}

entrada = int(input("Lista de contactos\n1 para adicionar um contacto\n0 para eliminar\n--> "))
if entrada == 1:
    nome = input("Introduza o nome que quer adicionar: ").lower()
    num = input("Digite o contacto telefónico: ")
    if num.isdigit():
        contactos[nome] = int(num)
        print("Contacto adicionado com sucesso!")
    else:
        print("Entrada inválida.")
elif entrada == 0:
    apagar = input("Introduza o nome do contacto que deseja eliminar: ").lower()
    if apagar in contactos:
        del contactos[apagar]
        print(f"Lista de contactos atualizada: \n{contactos}")
    else:
        print("Contacto não encontrado.")
else:
    print("Opção inválida.")

print(f"Lista de contactos: \n{contactos}")