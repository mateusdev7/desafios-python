from random import randint

s = 0
v = 0
while True:
    usuario_numero = int(input('Sua jogada (0 a 10): ').strip()) # Escolha do número
    while usuario_numero > 10:
        usuario_numero = int(input('Sua jogada (0 a 10): ').strip()) 

    usuario_escolha = str(input('Você quer par ou impar [P/I]: ').strip().upper()[0]) # Escolha do tipo
    while usuario_escolha not in 'PpIi':
        usuario_escolha = str(input('Você quer par ou impar [P/I]: ').strip().upper()[0])

    computador_numero = randint(0,10) # Jogada do computador
    total = usuario_numero + computador_numero # Soma das jogadas
    print(f'Você jogou {usuario_numero} e o computador {computador_numero}. Total de {total}')

    if usuario_escolha == 'P': # Se a escolha for PAR faça isso
        if total % 2 == 0:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif usuario_escolha == 'I': # Se a escolha for ÍMPAR faça isso
        if total % 2 == 1:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('-=-' * 10)
    print('Vamos jogar novamente xD')
    print('-=-' * 10)
print('-=-' * 10)
print(f'GAME OVER!!! Você venceu {v} vez(es).')
print('-=-' * 10)
    