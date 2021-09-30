from calendar import isleap
from datetime import date
from time import sleep

print('-=-' * 14)
print('Vamos analisar se o ano é bissexto ou não')
print('-=-' * 14)

ano = int(input('Qual ano você deseja saber? Digite "0" para analisar o ano atual\n>'))
print('PROCESSANDO...')
sleep(1)

if ano == 0:
    ano = date.today().year
ano_bissexto = isleap(ano)
if ano_bissexto is True:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
