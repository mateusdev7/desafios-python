lista = []
maior = 0 
menor = 0
for c in range(5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores {lista}\n')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) -> ', end='')
for i, v in enumerate(lista):
    if v == maior:
        if v > 1:
            print(f'({i}) ', end='')
        if v == 1:
            print(f'{i}', end='')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) -> ', end='')
for i, v in enumerate(lista):
    if v == menor:
        if v > 1:
            print(f'({i}) ', end='')
        if v == 1:
            print(f'{i}', end='')
print()

