from random import choice

print('====Desafio 019====')
print('Sorteando um aluno da lista')

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
