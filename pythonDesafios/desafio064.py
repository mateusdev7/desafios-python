n = cont = soma = 0
while n != 999:
    n = int(input(f'Digite um número[999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
if n == 999:
    print('O programa acabou')
print(f'A soma dos números é igual a {soma}')
print(f'Foram digitados um total de {cont} números.')