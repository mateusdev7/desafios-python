print('-=-' * 9)
print('Contagem de números e soma')
print('-=-' * 9)

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'\nExistem {cont} números impares e multiplos de 3 entre 1 e 500')
print(f'A soma entre esses números é igual a {soma}\n')