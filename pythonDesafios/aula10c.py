n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua media foi de {media:.2f}')
if media >= 7.0:
    print('PARABÉNS você foi aprovado!!!')
else:
    print('Infelizmente você não foi aprovado.')
    print('A nota necessária é no minímo 7.0.')
