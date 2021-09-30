def principal():
    peso = float(input('Qual o seu peso (Kg)?\n>'))
    altura = float(input('Qual a sua altura (m)?\n>'))
    imc = peso / (altura ** 2)
    print(f'O seu IMC é de {imc:.1f}Kg/m²\ne foi classificado como: {situacao_peso(imc)}')


def situacao_peso(imc):
    if imc < 18.5:
        situacao = 'Abaixo do peso normal, cuide-se!'
    elif 18.5 <= imc < 25:
        situacao = 'Peso ideal, PARABÉNS!!! '
    elif 25 <= imc < 30:
        situacao = 'Sobrepeso, cuide-se!'
    elif 30 <= imc < 40:
        situacao = 'Obesidade, cuide-se!'
    else:
        situacao = 'Obesidade mórbida, CUIDADO!!!'

    return situacao


principal()
