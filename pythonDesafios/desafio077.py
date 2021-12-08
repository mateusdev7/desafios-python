palavras = ('programar','aprender','estudar','comer','caminhar','jogar')
vogais = ("a","e","i","o","u")
consoantes = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z")
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(f'{letra}',end=' ')
    print(f'\nNa palavra {p.upper()} temos as consoantes: ', end='')
    for letra in p:
        if letra.lower() in consoantes:
            print(f'{letra}', end='')
    print()