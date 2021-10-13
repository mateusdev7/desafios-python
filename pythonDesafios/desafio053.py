frase = str(input('Digite uma frase: ').upper().replace(" ", ""))
if frase == frase[::-1]:
    print(f'A frase {frase} é um palíndromo')
    print(f'Pois, ela lida de trás pra frente é igual de frente pra trás: {frase[::-1]}')
else:
    print(f'A frase {frase} não é um palíndromo')
    