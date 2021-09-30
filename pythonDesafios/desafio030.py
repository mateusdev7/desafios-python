print('-=-' * 18)
print('Vamos identificar se o seu número é par ou impar')
print('-=-' * 18)

numero = int(input('Insira o número para identificarmos se é par ou impar\n>'))
resultado = numero % 2

if resultado == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')

'''n = int(input('Digite um número inteiro: '))
d = n/2
if d == int(d):
    print('O número é par')
else:
    print('O número é impar')'''
