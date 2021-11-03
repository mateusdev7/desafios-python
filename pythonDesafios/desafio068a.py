from random import randint

s = 0
v = 0
while True:
    jogador = int(input('Sua jogada (0 a 10): ').strip())
    while jogador > 10:
        print('Apenas entre 0 e 10')
        jogador = int(input('Sua jogada (0 a 10): ').strip())

    tipo = str(input('PAR ou ÍMPAR [P/I]: ').strip().upper()[0])
    while tipo not in 'PI':
        print('Apenas PAR ou ÍMPAR [P/I]')
        tipo = str(input('PAR ou ÍMPAR [P/I]: ').strip().upper()[0])
    computador = randint(0,10)
    total = jogador + computador

    if total % 2 == 0:
        situacao = 'PAR'
    else:
        situacao = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu {situacao}')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
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
print(f'GAME OVER!!! Você venceu {v} vez(es)')
print('-=-' * 10)