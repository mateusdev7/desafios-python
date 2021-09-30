import pygame

nome = str(input('Adivinhe o nome em que estou pensando\n>'))
if nome[:6].upper() == 'MATEUS':
    print('Parabéns você acertou')
    pygame.mixer.init()
    pygame.mixer.music.load('acertou.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print('Você errou, tente novamente eu confio em você!!!')
    pygame.mixer.init()
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
