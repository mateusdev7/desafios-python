from random import randint
import pygame
from time import sleep


print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!!!')
print('-=-' * 19)

usuario = int(input('Em qual número eu pensei? \n>').strip())
computador = randint(0, 5)  # Faz o computador pensar em um número...
print('PROCESSANDO...')
sleep(2)
if usuario == computador:  # Se o número que o usuário pensar for igual o do computador...
    print(f'Parabéns, você acertou eu pensei exatamente no número {computador}.')
    pygame.mixer.init()
    pygame.mixer.music.load('acertou.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:  # Se não for igual o que o computador pensou...
    print(f'ERROU!!! Eu pensei no número {computador} e você escolheu {usuario}.')
    pygame.mixer.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
