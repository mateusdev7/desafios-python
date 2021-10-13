from datetime import date

ano_atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1,8):
    nascimento = int(input(f'Em qual ano a {c}º pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Encontramos {totalmaior} pessoa(s) maiore(s) de idade.')
print(f'Encontramos {totalmenor} pessoa(s) menore(s) de idade.')
