while True:
    print('=======================================================================')
    print('Tabuada automática. Digite um número negativo para encerrar o programa')
    print('=======================================================================')
    numero = int(input('Você deseja saber a tabuada de qual número?\n>'))
    if numero < 0:
        print('\nO programa foi encerrado. Volte sempre para divertir-se com a matemática. <3\n')
        break
    for c in range(1,11):
        print(f'{numero} x {c} = {numero * c}')
    