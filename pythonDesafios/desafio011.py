largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da parede: "))
area = largura * altura
print(f'Sua parede tem dimensões de {largura}x{altura} e a sua área é de {area}m²')
litros = area / 2
print(f'Para pintar essa parede, você precisará de {litros} litros de tinta')
