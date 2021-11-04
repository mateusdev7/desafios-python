from os import replace


total_gasto = produto1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ').strip())
    preco = float(input('Preço do produto(Obs: Use . como separador): R$'))
    cont += 1
    while preco < 0:
        preco = float(input('Preço do produto: R$'))
    total_gasto += preco

    if preco > 1000:
        produto1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = str(input('Quer cadastrar outro produto [S/N]? ').upper().strip()[0])
    while opcao not in 'SN':
        opcao = str(input('Quer cadastrar outro produto [S/N]? ').upper().strip()[0])
    if opcao == 'N':
        print('-------- PROGRAMA ENCERRADO --------')
        break
print(f'O total gasto foi de R${total_gasto:.2f}')
print(f'{produto1000} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi a/o {barato} e ele custa R${menor:.2f}')
