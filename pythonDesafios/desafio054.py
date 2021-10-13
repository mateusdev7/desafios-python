from datetime import date # Importando a biblioteca da data atual

ano_atual = date.today().year # Pegando o ano atual
totalmaior = 0 # Soma das pessoas maiores de idade
totalmenor = 0 # Soma das pessoas menores de idade
for c in range(1,8): # Perguntando a idade de 7 pessoas
    nascimento = int(input(f'Em qual ano a {c}º pessoa nasceu? '))
    idade = ano_atual - nascimento # Idade atual da pessoa
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Encontramos {totalmaior} pessoa(s) maiore(s) de idade.')
print(f'Encontramos {totalmenor} pessoa(s) menore(s) de idade.')
