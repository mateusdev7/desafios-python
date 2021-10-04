from time import sleep

print('-=-'*10)
print('Números pares de 1 a 50')
print('-=-' * 10)

for par in range(2, 51, 2):
    sleep(0.3)
    print(par)
