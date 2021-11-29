times = ('Atlético-MG','Palmeiras','Flamengo','Bragantino','Fortaleza','Corinthians','Internacional','Fluminense','Cuiabá','Ceará SC',
'Atlético-PR','América-MG','Atlético-GO','São Paulo','Bahia','Santos','Juventude','Grêmio','Sport Recife','Chapecoense')

print(f'Lista dos 20 primeiros times do brasileirão\n {times}')

# 1º) Apenas os 5 primeiros colocados
print('\n======== Os 5 primeiros times são ========\n')
for times5 in times[:5]:
    print(f'{times5}')
# 2º) O ultimos 4 colocados da tabela
print('\n======== Os 4 últimos times são ========\n')
for ultimos4 in times[16:21]:
    print(f'{ultimos4}')
# 3º) Uma lista com os times em ordem alfabética
print('\n======== Os times em ordem alfabética ========\n')
print(sorted(times[:21]))
# 4º) Em qual posiçõa da tabela está o time da Chapecoense
indice_chapeco = times.index('Chapecoense')
print('\n======== Colocação do time da Chapecoense ========\n')
print(f'O time da Chapecoense está em {indice_chapeco+1}º lugar')
print()