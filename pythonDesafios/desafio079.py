lista = []

nome = str(input('Qual é o seu nome? '))
print(f'Olá, {nome} vamos começar...\n')
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Esse valor já está na lista, não podemos adicionar valores repetidos')
    if valor not in lista:
        lista.append(valor)
    opcao = str(input('Quer inserir outro valor [S/N]? ').upper().strip()[0])
    while opcao not in 'SN':
        opcao = str(input('Quer inserir outro valor [S/N]?').upper().strip()[0])
    if opcao == 'N':
        print("\n========== PROGRAMA ENCERRADO ==========")
        break
lista.sort()
print(f'Olá {nome} você inseriu os valores {lista}')