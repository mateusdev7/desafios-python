from random import randint
from time import sleep
import pygame


print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10, tente adivinhar!!!')
print('-=-' * 19)

cont = 0
usuario = int(input('\nEscolha um número entre 0 e 10: ').strip())
computador = randint(0, 10) # O computador sorteia um número de 0 a 10
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
    print(f'Precisou de {cont + 1} tentativa(s) para acertar')
    pygame.mixer.init()
    pygame.mixer.music.load('acertou.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    