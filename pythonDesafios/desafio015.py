dias = int(input("Por quantos dias você alugou o carro? "))
km = float(input("Quantos km você percorreu com o carro? "))
pago = (dias * 60) + (km * 0.15)
print(f'O total a ser pago é de R${pago:.2f}!')
