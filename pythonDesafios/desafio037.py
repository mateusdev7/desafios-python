def principal():
    print('-=-' * 15)
    print('Conversor de bases (Binário, Octal, Hexadecimal')
    print('-=-' * 15)

    print('\nPara qual base você deseja converter?')
    print('[ 1 ]Converter para Binário [ 2 ]Converter para Octal [ 3 ]Converter para Hexadecimal')
    escolha = int(input('>'))

    if escolha == 1:
        numero = int(input('Qual número você deseja converter para binário?\n>'))
        print(f'O número {numero} em binário é: {bin(numero)[2::]}')
    elif escolha == 2:
        numero = int(input('Qual número você deseja converter para Octal?\n>'))
        print(f'O número {numero} em octal é: {oct(numero)[2::]}')
    elif escolha == 3:
        numero = int(input('Qual número você deseja converter para Hexadecimal?\n>'))
        print(f'O número {numero} em hexadecimal é: {hex(numero)[2::]}')
    else:
        print('Opção invalida, tente uma das listadas acima!!!')


principal()
