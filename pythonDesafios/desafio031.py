from time import sleep
print('-=-' * 15)
print('Iremos calcular o preço da sua viagem (R$)')
print('-=-' * 15)

distancia = float(input('Qual a distância da viagem?\n>'))
print('CALCULANDO...')
sleep(2)

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da sua viagem vai custar R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O preço da sua viagem vai custar R${preco:.2f}')
