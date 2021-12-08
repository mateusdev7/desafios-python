listagem = ('Caderno', 10.90, 'Lápis', 1.50, 'Borracha', 1.00, 'Apontador', 1.50, 'Caneta', 2.00)

print('=' * 45)
print(f'{"LISTAGEM DE PREÇOS DE CADA PRODUTO":^45}')
print('=' * 45)
print(
    f'{listagem[0]:.<30}R${listagem[1]:>5.2f}\n'
    f'{listagem[2]:.<30}R${listagem[3]:>5.2f}\n'
    f'{listagem[4]:.<30}R${listagem[5]:>5.2f}\n'
    f'{listagem[6]:.<30}R${listagem[7]:>5.2f}\n'
    f'{listagem[8]:.<30}R${listagem[9]:>5.2f}'
)
print('=' * 45)