preco1 = float(input("Qual o preço atual do produto? R$"))
preco2: float = (preco1*5)/100
print(f"Com 5% de desconto em cima de R${preco1:.2f} o preço do produto diminui R${preco2:.2f}")
preco3 = preco1 - preco2
print(f"Portanto, o preço final será de R${preco3:.2f}")
