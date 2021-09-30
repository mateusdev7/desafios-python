# Trabalhando com cores no terminal

x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
media = (x + y) / 2
if media >= 6:
    print(f'Parabens você foi aprovador com a media {media}')
else:
    print(f'Sua \033[31mmédia {media}\033[m não foi suficiente... Continue estudando')
