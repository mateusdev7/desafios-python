import random
maior = menor = 0

sorteio = tuple(random.sample(range(10),5))
print('Os valores sorteados são: ', end='')
for n in sorteio:
    print(f'{n} ', end='')
print(f'O maior valor sorteado foi {max(sorteio)} o menor valor sorteado foi {min(sorteio)}')