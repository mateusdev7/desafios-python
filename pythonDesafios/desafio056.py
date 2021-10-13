# ----- O que deve ser feito -----
# A média de idade do grupo.
# Qual é o nome do HOMEM mais VELHO.
# Quantas MULHERES tem MENOS de 20 anos.

somaidade = 0 # Para somar as idades.   
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'---- {c}º Pessoa ----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip().upper()
    somaidade += idade # Somatório de idades para, posteriormente tirar a média.

    # Se for o primeiro da lista o programa ja escolher ele.
    if c == 1 and sexo in 'Mm': # Procura o sexo masculino como M ou m.
        maior_idade_homem = idade
        nome_velho = nome
    # Se não, ele vai procurar o homem mais velho e a idade.
    if sexo in 'Mm' and idade > maior_idade_homem: 
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20: # Procura o sexo masculino como F ou f.
        totmulher20 += 1

mediaidade = somaidade / 4 # Executa a média das idades.

print(f'A média de idade do grupo é {mediaidade} anos')
print(f'A idade do homem mais velho é de {maior_idade_homem} anos e ele se chama {nome_velho}.')
print(f'Existe(m) {totmulher20} mulher com menos de 20 anos.')
