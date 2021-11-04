total18 = total_homem = total_mulher = 0
while True:
    print('--------------------')
    print('CADASTRE UMA PESSOA')
    print('--------------------')
    idade = int(input('Digite a idade: ').strip())
    sexo = str(input('Digite o sexo [M/F]: ').upper().strip()[0])
    while sexo not in 'MF':
        print('Sexo INVÁLIDO! Insira novamente.')
        sexo = str(input('Digite o sexo [M/F]: ').upper().strip()[0])
    if idade >= 18:
        total18 += 1
    if sexo in 'Mm':
        total_homem += 1
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1

    opcao = str(input('Quer continuar [S/N]? ').upper().strip()[0])
    while opcao not in 'SN':
        print('Opção INVÁLIDA! Insira novamente.')
        opcao = str(input('Quer continuar [S/N]? ').upper().strip()[0])
    if opcao == 'N':
        print('====== FIM DO PROGRAMA ======')
        break

print(f'Total de pessoas acima de 18 anos: {total18}')
print(f'Total de homens cadastrados: {total_homem}')
print(f'Total de mulher abaixo de 20 anos: {total_mulher}')
print('====== FIM DO PROGRAMA ======')
