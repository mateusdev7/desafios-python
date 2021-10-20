from time import sleep
escolha = 123
while escolha != 0:
    print('============Cadastro de sexo============')
    print('\n[ 1 ] Cadastrar um sexo [ 0 ] Sair do programa')
    escolha = int(input('\nDigite uma das opções acima\n>'))

    if escolha == 1:
        sexo = str(input('Qual o sexo a ser registrado [M/F]?')).strip().upper()[0]
        while sexo not in 'MmFf':
            sexo = str(input('Sexo inválido. Insira corretamente [M/F]: ')).strip().upper()[0]
        sleep(1)
        if sexo in 'Mm':
            print('\nSexo MASCULINO registrado com sucesso.\n')
        elif sexo in 'Ff':
            print('\nSexo FEMININO registrado com sucesso.\n')
    elif escolha == 0:
        print('Você saiu do programa')
