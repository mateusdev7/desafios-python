def triangulo_qualquer():
    # Usuário inserindo os seguimentos do triângulo
    l1 = float(input('Primeiro seguimento: '))
    l2 = float(input('Segundo seguimento: '))
    l3 = float(input('Terceiro seguimento: '))
    # Condição para formação do triângulo
    if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
        print('Os seguimentos acima podem formar um triângulo equilátero ', end='')
        '''Esse "if" está para dentro do outro "if", pois, se o triângulo puder existir ele vai falar qual o tipo dele, 
        se não ele vai dizer que não pode existir, pulando para o "else" lá em baixo'''
        if l1 == l2 == l3:
            print('EQUILÁTERO')
        # Condição de existência do triângulo equilátero
        elif l1 != l2 != l3 != l1:
            print('ESCALENO')
        # Condição de existência do triângulo escaleno
        elif (l1 == l2) != l3 and (l2 == l3) != l1 and (l3 == l1) != l2:
            print('ISÓSCELES')
        # Condição de existência do triângulo isósceles
        # OBS: Eu poderia ter usando um ELSE no lugar de ELIF, tornando desnecessário esse ELIF.
    else:
        print('Com esses seguimentos não é possível formar um triângulo')


triangulo_qualquer()
