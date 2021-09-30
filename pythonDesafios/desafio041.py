from datetime import date


def dados():
    ano_nascimento = int(input('Qual o seu ano de nascimento?\n>'))
    idade = date.today().year - ano_nascimento
    print(f'Como você tem {idade} anos,')
    print(f'você está alocado na categoria: \033[1;31m{categoria_dados(idade)}\033[m.')


def categoria_dados(idade):
    if idade <= 9:
        categoria = 'MIRIM'
    elif idade <= 14:
        categoria = 'INFANTIL'
    elif idade <= 19:
        categoria = 'JUNIOR'
    elif idade <= 20:
        categoria = 'SÊNIOR'
    else:
        categoria = 'MASTER'

    return categoria


dados()
