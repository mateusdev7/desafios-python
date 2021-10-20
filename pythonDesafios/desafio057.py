sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação Inválida. Insira o sexo [M/F]: ')).upper().strip()[0]
if sexo in 'Mm':
    print('Sexo Masculino registrado com sucesso')
if sexo in 'Ff':
    print('Sexo Feminino registrado com sucesso')

