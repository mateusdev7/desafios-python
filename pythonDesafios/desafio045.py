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
        print('O jogo empatou.')
    elif jogador == 1:  # Papel
        print('O Usuário venceu.')
    elif jogador == 2:  # Tesoura
        print('O Computador venceu.')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:  # Pedra
        print('O Computador venceu.')
    elif jogador == 1:  # Papel
        print('O jogo empatou.')
    elif jogador == 2:  # Tesoura
        print('O Usuário venceu.')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:  # Pedra
        print('O Usuário venceu.')
    elif jogador == 1:  # Papel
        print('O Computador venceu.')
    elif jogador == 2:  # Tesoura
        print('O jogo empatou.')
    else:
        print('JOGADA INVÁLIDA')
