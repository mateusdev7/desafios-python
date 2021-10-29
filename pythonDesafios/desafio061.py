primeiro_termo = int(input('Digite o primeiro termo de uma P.A: '))
razao = int(input('Digite a razão dessa P.A: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
print('FIM')