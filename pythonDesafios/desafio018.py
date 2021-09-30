from math import radians, sin, cos, tan

angulo = int(input('Digite o valor de um ângulo: '))
sen = sin(radians(angulo))  # Pegando o valor em radianos e convertendo para seno
cos = cos(radians(angulo))  # Pegando o valor em radianos e convertendo para cosseno
tg = tan(radians(angulo))  # Pegando o valor em radianos e convertendo para tangente
print(f'O seno desse ângulo é {sen:.2f}\nO cosseno desse ângulo é {cos:.2f}\nA tangente desse ângulo é {tg:.2f}')

# seno, cosseno e tangente
