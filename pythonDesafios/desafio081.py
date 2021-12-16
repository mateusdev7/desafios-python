from time import sleep

lista_de_numeros = []
while True:
    lista_de_numeros.append(int(input('Digite um valor: ').strip()))
    opcao = str(input('Quer inserir outro valor [S/N]? ').upper().strip()[0])
    while opcao not in 'SN':
        opcao = str(input('Quer inserir outro valor [S/N]?').upper().strip()[0])
    if opcao == 'N':
        print(f'\n{"Somando a quantidade de números em sua lista":>50}')
        break

sleep(1)
print('-=' * 30)
print(f'Foram digitados {len(lista_de_numeros)} números')
print('-=' * 30)
print()

print(f'{"Colocando sua lista de números de forma decrescente":>55}')
print('-=' * 30)
sleep(1)
lista_de_numeros.sort(reverse = True)
for n in lista_de_numeros:
    print(n)
print('-=' * 30)
print(f'\n{"Analisando se o número 5 está ou não na lista":>50}')
sleep(2)
print('-=' * 30)
if 5 in lista_de_numeros:
    print(f'O número 5 está na lista foi digitado na {lista_de_numeros.index(5)}º posição')
else:
    print('O número 5 não está na lista.')
