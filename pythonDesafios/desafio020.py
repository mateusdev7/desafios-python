from random import shuffle
print('====Desafio 020====')
print('Sorteando a sequência de apresentação')
n1 = str(input('Aluno 01: '))
n2 = str(input('Aluno 02: '))
n3 = str(input('Aluno 03: '))
n4 = str(input('Aluno 04: '))
n5 = str(input('Aluno 05: '))


lista = [n1, n2, n3, n4]
shuffle(lista)

print(f'A sequência de apresentação será')
print(lista)

'''Com o "Sample" a gente pode escolher a quantidade de alunos que vão ser sorteados, limitando a quantidade de alunos
usando o K= (algum valor)'''
'''Podemos usar também o "shuffle" para fazer isso, porém com o shuffle não da pra limitar a quantidade de alunos
que serão sorteados'''
