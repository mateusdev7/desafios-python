pares = 0
numeros = tuple(int(input(f'Digite um número:\n'))for c in range(1,5))

print(f'\nO número 9 apareceu {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3) + 1}º posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
for n in numeros:
    if n % 2 == 0:
        print(f'Foram digitados {n} números pares')
        break
