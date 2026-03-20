"""Crie um programa em Python para gerenciar uma lista de notas (float). O programa deve realizar as seguintes operações, utilizando as funções do tipo List:

Ler do usuário 5 notas inteiras e armazená-las em uma list.
Ordenar a listusando sort().
Criar uma cópia da list com tamanho maior (7 posições), preenchendo as novas posições com 0.
Copiar apenas as 3 primeiras notas (já ordenadas) para uma nova list .
Comparar se a list original (ordenado) e o list copiado das 3 primeiras notas são iguais.
Criar uma nova list com 5 posições preenchidas com o valor -1 usando list comprehension.
Imprimir todos as lists criadas em cada etapa.
Exemplo de funcionamento esperado:Notas lidas: [40, 20, 50, 30, 10]
Notas ordenadas: [10, 20, 30, 40, 50]
Cópia com tamanho maior: [10, 20, 30, 40, 50, 0, 0]
Primeiras 3 notas (cópia): [10, 20, 30]
São iguais (original e primeiras 3)? false
List preenchido com -1: [-1, -1, -1, -1, -1]"""

if __name__ == "__main__":
    lista_notas = []    
    for nota in range(5):
        nota = float(input("Digite o valor da nota: "))            
        lista_notas.append(nota)
    print(f"Notas inseridas: {lista_notas}")
    lista_ordenada = lista_notas.copy()
    lista_ordenada.sort()
    print(f"Notas ordenadas: {lista_ordenada}")
    lista_copia = lista_ordenada + [0, 0]
    print(f"Cópia com tamanho maior: {lista_copia}")    
    print(f"Primeiras 3 notas: {lista_copia[0:3]}")

    print(f"São iguais (original e primeiras 3)? {True}") if lista_notas[0:3] == lista_copia[0:3] else print(f"São iguais (original e primeiras 3)? {False}")
    
    lista_preenchida = [-1 for i in range(5)]
    print(f"List preenchido com -1: {lista_preenchida}")