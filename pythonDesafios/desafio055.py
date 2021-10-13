lista = [] # Lista vazia para inserir os pesos

for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}º pessoa em Kg: '))
    lista += [peso]
print(f'O maior peso foi o: {max(lista):.2f}Kg') # Maior valor da lista
print(f'O menor peso foi o: {min(lista):.2f}Kg') # Menor valor da lista
