num1 = int(input('Insira um número: ').strip())
num2 = int(input('Insira outro número: ').strip())

opcao = 123
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior número 
    [ 4 ] Novos números 
    [ 5 ] Sair do programa''')
    opcao = int(input('\nQual opção você deseja?\n>').strip())

    if opcao == 1:
        soma = num1 + num2
        print('===========================================')
        print(f'A soma entre {num1} e {num2} resulta em {soma}')
        print('===========================================')
    
    elif opcao == 2:
        multiplicar = num1 * num2
        print('===================================================')
        print(f'A multiplicação entre {num1} e {num2} resulta em {multiplicar}')
        print('===================================================')
    elif opcao == 3:
        if num1 > num2:
            print('===================================')
            print(f'O maior número entre {num1} e {num2} é {num1}')
            print('===================================')
        elif num2 > num1:
            print('===================================')
            print(f'O maior número é {num1} e {num2} é {num2}')
            print('===================================')
        elif num1 == num2:
            print('============================')
            print('Os dois números são iguais')
            print('============================')
    elif opcao == 4:
        print('Quais são os novos números?\n')
        num1 = int(input('Insira o primeiro novo número: ').strip())
        num2 = int(input('Insira o segundo novo número: ').strip())
else:
    print('Você saiu do programa.')
    
    