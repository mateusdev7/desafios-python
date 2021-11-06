numeros_tupla = ('Zero','Um','Dois','Trê','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze',
'Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    usuario_numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= usuario_numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros_tupla[usuario_numero]}')