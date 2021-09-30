real = float(input("Informe o saldo da sua carteira: R$"))
dolar = real/5.36 #o valor deve ter um ponto e não a virgula, caso coloque a virgula o programa não funciona!!
print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
