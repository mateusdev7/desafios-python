soma = 0
cont = 0
cont1 = 0
soma1 = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
    elif num % 2 != 0:
        soma1 += num
        cont1 += 1
print(f'Você digitou um total de {cont} número(s) PARE(S) e {cont1} número(s) IMPARE(S)')
print(f'A soma dos números pares foi de {soma}')
print(f'A soma dos números impares foi de {soma1}')
