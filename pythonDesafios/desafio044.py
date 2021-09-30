print('====LOJAS RAIZEN====')
total = float(input('Preço total das contas: R$'))
print('FORMA DE PAGAMENTO:')
print('(1) à vista dinheiro/cheque\n(2) à vista cartão')
print('(3) 2x no cartão\n(4) 3x no cartão ou mais')
escolha = int(input('>'))

if escolha == 1:
    desconto = (10 * total) / 100
    print(f'Com pagamento a vista (dinheiro/chque) você ganha 10% de desconto, equivalendo a R${desconto:.2f}')
    print(f'Pagando um valor total de R${total - desconto:.2F}')
elif escolha == 2:
    desconto2 = (5 * total) / 100
    print(f'Com pagamento à vista no cartão, você ganha 5% de desconto, equivalendo à R${desconto2:.2f}')
    print(f'Pagando um valor total de R${total - desconto2:.2f}')
elif escolha == 3:
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
    print(f'Pagando um valor total de R${total:.2f}')
elif escolha == 4:
    parcela = int(input('Em quantas vezes você vai dividir? '))
    juros = (20 * total) / 100
    print(f'Sua compra será parcelada em {parcela}x de R${(juros + total) / parcela:.2f} COM JUROS de 20%.')
    print(f'Sendo assim, sua compra de R${total:.2f} vai passar a custar R${juros + total:.2f}')
else:
    print('Essa opção não está listada acima!!!')
