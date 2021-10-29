total = soma = maior = menor = 0
opcao = 'S'
while opcao in 'Ss':
    n = int(input(f'Digite um número: ').strip())
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Você quer digitar outro número [S/N]?').upper().strip()[0])
media = soma / total
print('-=-' * 13)
print(f'A média entre os valores é igual a {media}')
print('-=-' * 15)
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
print('-=-' * 15)
