def notas():
    n1 = float(input('Insira a primeira nota do aluno\n>'))
    n2 = float(input('Insira a segunda nota do aluno\n>'))
    media = (n1 + n2) / 2
    print(f'A sua média equivale a {media}')
    print(f'E a sua situação é: {situacao_notas(media)}')


def situacao_notas(media):
    if media < 5:
        situacao = 'REPROVADO'
    elif 5 <= media <= 6.9:
        situacao = 'RECUPERAÇÃO'
    else:
        situacao = 'APROVADO'

    return situacao


notas()
