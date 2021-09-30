from datetime import date

# Variáveis de ano de nascimento, ano atual e idade do indivíduo, respectivamente.
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'\n\033[1;34mQuem nasceu no ano de {ano_nascimento} tem {idade} anos em {ano_atual}.\033[m')
if idade < 18:
    # Caso o usuário seja menor de idade.
    print(f'\n\033[1;31mAinda falta(m) {18 - idade} ano(s)\033[m para o seu alistamento militar.')
    print(f'Portanto, \033[1;31mele será em {ano_nascimento + 18}.\033[m')
elif idade == 18:
    # Caso o usuário já seja maior de idade.
    print('\033[1;31mSeu alistamento é nesse ano. Não esqueça de fazê-lo.\033[m')
else:
    # Caso o usuário já seja maior de idade e não se alistou.
    print(f'O seu alistamento foi há \033[1;31m{idade - 18} anos atrás,\033[m')
    print(f'ou seja, ele ocorreu em \033[1;31m{ano_nascimento + 18}.\033[m')
