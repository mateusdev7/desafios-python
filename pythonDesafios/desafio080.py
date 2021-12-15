# lista_de_numeros = []

# for n in range(1,6):
#     numero_usuario = int(input(f'Digite o {n}º número: '))
#     while len(lista_de_numeros) == 0 or numero_usuario < lista_de_numeros[0]:
#         lista_de_numeros.insert(0, numero_usuario)
#         print("Número adicionado na posição 0 da lista")
#     while len(lista_de_numeros) > 1

lista_de_numeros = []

for c in range(1,6):
    numero_usuario = int(input(f'Digite o {c}º número: '))
    if c == 1 or numero_usuario > lista_de_numeros[-1]:
        lista_de_numeros.append(numero_usuario)
        print('Número adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista_de_numeros):
            if numero_usuario <= lista_de_numeros[posicao]:
                lista_de_numeros.insert(posicao, numero_usuario)
                break
            posicao += 1
print('-=-' * 30)
print(f"Os números digitados na ordem crescente foram {lista_de_numeros}")
