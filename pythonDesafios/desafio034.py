salario = float(input('Informe o seu salário\n>R$'))
if salario > 1250:
    salario1 = salario * 1.1
    print(f'Com um aumento de 10% seu novo salário será de R${salario1:.2f}')
if salario <= 1250:
    salario2 = salario * 1.15
    print(f'Com um aumento de 15% seu novo salário será de R${salario2:.2f}')
