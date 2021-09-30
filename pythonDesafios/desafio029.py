print('-=-' * 6)
print('Radar Eletrônico')
print('-=-' * 6)
velocidade = int(input('Qual é a velocidade atual do carro (Km/h)?\n>'))
if velocidade > 80:
    print('OPA!!! Você excedeu o limite de velocidade que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print(f'Portanto, você deve pagar uma multa de R${multa:.2f}.')
print('Tenha um bom dia e dirija com segurança.')
