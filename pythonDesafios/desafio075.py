pares = 0
numeros = tuple(int(input(f'Digite um número:\n'))for c in range(1,5))

numero_nove = numeros.count(9)
numero_tres = numeros.index(3)
print(f'O número 9 apareceu {numero_nove} vez(es)')
print(f'O número 3 foi digitado na {numero_tres + 1}º posição')
for n in numeros:
    if n % 2 == 0:
        pares += 1
print(f'Foram digitados {pares} números pares')
