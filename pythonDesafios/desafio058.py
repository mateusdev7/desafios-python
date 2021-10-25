from random import randint
from time import sleep

opcao = 123
cont = 0
while opcao != 0:
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 10, quer tentar adivinhar?')
    print('-=-' * 20)
    print('\n[ 1 ] Sim [ 0 ] Não')
    opcao = int(input('Escolha uma das opções acima\n>'))

    if opcao == 1:  
        computador = randint(0, 10) # O computador sorteia um número de 0 a 10
        usuario = int(input('\nEscolha um número entre 0 e 10: ').strip())   
        cont += 1
        while usuario != computador:
            if usuario < computador:
                print('Mais... Tente novamente')
            else:
                print('Menos... Tente novamente')
            usuario = int(input('Insira outro número: '))
            cont += 1
        if usuario == computador:
            print('\nPARABÉNS. Você ACERTOU!!!')
            print('Calculando a quantide de tentivas necessárias...')
            sleep(1)
            print('-=-' * 15)
            print(f'Você precisou de {cont} tentativa(s) para acertar.')
            print('-=-'* 15)
    elif opcao == 0:
        print('Você saiu do jogo.')