nome = str(input('Digite o seu nome completo\n>').strip())
print('Analisando seu nome...')
print(f'Seu nome em letras minuscula é {nome.lower()}')
print(f'Seu nome em letras maiusculas é {nome.upper()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
