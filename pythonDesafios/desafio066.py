soma = quantidade = 0
while True:
    n = int(input('Digite um número [999 encerra o programa]: '))
    if n == 999:
        break
    soma += n
    quantidade += 1
print(f'A soma dos {quantidade} valores digitados foi de {soma}')
