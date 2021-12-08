a = [2,3,4,7]
b = a # Juntando duas listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

c = [1,2,3,4]
d = a[:] # Fazendo uma cópia da lista C para a lista D
d[2] = 8

print(f'\nLista C: {c}')
print(f'Lista D: {d}')
