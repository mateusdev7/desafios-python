import math

print('===Desafio 017===')
print('Medindo o cateto do triângulo retângulo')

ca = float(input('Comprimento do caceto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
# Utilizamos o metódo "hypot"
