from time import sleep

#U+1F973 (Emoji de comemoração)

print('-=-' * 7)
print('\033[1;31mContagem regressiva\033[m')
print('-=-' * 7)

for cont in range(10, -1, -1):
    sleep(0.5)
    print(cont)
print('\033[1;32mEXPLOSÃO DE FOGOS DE ARFICIOS\033[m \U0001F973')
