from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Escolha uma das opções abaixo:')
print('-=-' * 5)
print('''( 0 ) Pedra
( 1 ) Papel
( 2 ) Tesoura''')
print('-=-' * 5)
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=-' * 8)
print(f'Computador jogou {itens[computador]}')
print(f'Usuário jogou {itens[jogador]}')
print('-=-' * 8)

if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:  # Pedra
        print('\nO jogo empatou.')
    elif jogador == 1:  # Papel
        print('\nO Usuário venceu.')
    elif jogador == 2:  # Tesoura
        print('\nO Computador venceu.')
    else:
        print('\nJOGADA INVÁLIDA')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:  # Pedra
        print('\nO Computador venceu.')
    elif jogador == 1:  # Papel
        print('\nO jogo empatou.')
    elif jogador == 2:  # Tesoura
        print('\nO Usuário venceu.')
    else:
        print('\nJOGADA INVÁLIDA')
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:  # Pedra
        print('\nO Usuário venceu.')
    elif jogador == 1:  # Papel
        print('\nO Computador venceu.')
    elif jogador == 2:  # Tesoura
        print('\nO jogo empatou.')
    else:
        print('\nJOGADA INVÁLIDA')
