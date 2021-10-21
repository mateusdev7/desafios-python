from random import randint
from time import sleep

opcao = 123
cont = 0
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10, quer tentar adivinhar?')
print('-=-' * 19)
while opcao != 0:
    print('\n[ 1 ] Tentar adivinhar [ 0 ] Sair do jogo')
    opcao = int(input('Escolha uma das opção acima\n>'))

    if opcao == 1:  
        computador = randint(0, 10) # O computador sorteia um número de 0 a 10
        usuario = int(input('\nEscolha um número entre 0 e 10: ').strip())   
        while usuario != computador:
            if usuario < computador:
                print('Mais... Tente novamente')
            else:
                print('Menos... Tente novamente')
            usuario = int(input('Insira outro número: '))
            cont += 1
        if usuario == computador:
            print('PARABÉNS. Você ACERTOU!!!')
            print('Calculando a quantide de tentivas necessárias...')
            sleep(1)
            print('-=-' * 19)
            print(f'Precisou de {cont + 1} tentativa(s) para acertar')
            print('-=-'* 19)
    elif opcao == 0:
        print('Você saiu do jogo')