primeiro_termo = int(input('Digite o primeiro termo de uma P.A: '))
razao = int(input('Digite a razão dessa P.A: '))
decimo = primeiro_termo + (10-1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('Acabou')
