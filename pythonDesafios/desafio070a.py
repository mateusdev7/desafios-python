valor = int(input("Qual valor você quer sacar? R$ "))
cedulas = valor // 50 # Quantidade de cédulas
resto = valor % 50 # Resto da divisão para saber a quantidade das próximas cédulas

print('==' * 28)
print('Abaixo estão as informações das cédulas a serem sacadas')
print('==' * 28)
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$50,00')
cedulas = resto // 20 # Quantidade de cédulas de R$20,00
resto = resto % 20 # Resto da divisão por 20 (Deixa guardado)
if cedulas > 0:
    print(f'Total de {cedulas} cédula(s) de R$20,00')
cedulas = resto // 10 # Quantidade de cédulas de R$10,00
resto = resto % 10 # Resto da divisão por 10 (Deixa guardado)
if cedulas > 0: 
    print(f'Total de {cedulas} cédula(s) de R$10,00')
cedulas = resto // 1 # Quantidade de moedas de R$1,00
if cedulas > 0:
    print(f'Total de {cedulas} moeda(s) de R$1,00')
print('==' * 28)
print('Volte sempre ao banco RAIZEN. Tenha um bom dia!\n')