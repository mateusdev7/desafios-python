def principal():
    print('\033[33m-=-\033[m' * 17)
    print('Fazendo uma simulação de empréstimo para uma casa')
    print('\033[33m-=-\033[m' * 17)

    nome = str(input('Qual é o seu nome?\n>'))
    casa = float(input('Qual o valor da casa?\n>R$'))
    salario = float(input('Qual o seu salário?\n>R$'))
    anos = int(input('Quantos anos de financiamento?\n>'))
    prestacao = (casa / anos) / 12
    print(f'Para pagar uma casa no valor de R${casa:.2f} em {anos} anos, custará mensalmente o valor de '
          f'\033[1;32mR${prestacao:.2f}.\033[m')
    if prestacao > (30 * salario) / 100:
        print(f'{nome}, infelizmente o seu empréstimos foi \033[1;31mnegado\033[m, pois, a prestação excede 30% do seu '
              f'salário.')
        print(f'30% do seu salário equivale a {(30 * salario) / 100:.2f}, portanto, a prestação o excedeu.')
    elif prestacao <= (30 * salario) / 100:
        print(f'PARABÉNS {nome}, o seu empréstimo foi \033[1;34maprovado!!!\033[m')
        print(f'Você irá pagar durante {anos} anos, um valor mensal de \033[1;32mR${prestacao:.2f}\033[m.')


principal()
