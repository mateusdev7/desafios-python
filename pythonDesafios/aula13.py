for c in range(0, 6, 2):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

# f+1 significa para ele usar o número final que colocarmos, pelo fato dele não ir ate o fim.

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma é igual a {s}')
