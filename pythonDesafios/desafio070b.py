valor = int(input('Qual valor deseja sacar? R$'))
cedulas = valor // 100 # Quantidae de cédulas
resto = valor % 100 # Resto para saber as outras cédulas
print('==' * 28)
print('Abaixo estão as informações das cédulas a serem sacadas')
print('==' * 28)
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$100,00')
cedulas = resto // 50 # Quantidade de cédulas de R$50,00
resto %= 50 # Resto da divisão por R$50,00
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$50,00')
cedulas = resto // 20
resto %= 20
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$20,00')
cedulas = resto // 10
resto %= 10
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$10,00')
cedulas = resto // 5
resto %= 5
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$5,00')
cedulas = resto // 2
resto %= 2
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$2,00')
cedulas = resto // 1
if cedulas > 0:
    print(f'Total de {cedulas} moeda(s) de R$1,00')
print('==' * 28)
print('Volte sempre ao banco RAIZEN. Tenha um bom dia!\n')