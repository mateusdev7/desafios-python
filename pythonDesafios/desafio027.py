n = str(input('Digite o seu nome completo\n>').strip())
nome = n.split()
print(f'Muito prazer em te conhecer, {nome[0]}')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome) - 1]}')
