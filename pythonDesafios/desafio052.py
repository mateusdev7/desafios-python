numero = int(input('Digite um número: '))

primos = []

for a in range(1, numero + 1):
    if numero % a == 0:
        primos.append(a)
    else:
        pass

if len(primos) == 2:
    print(f'O número {numero} foi dividido por {primos}')
    print('Portanto, ele É PRIMO')
else:
    print(f'O número {numero} foi dividido por {primos}')
    print(f'Portanto, ele NÃO É PRIMO')
