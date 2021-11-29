numeros_tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze',
'Quartoze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    usuario = int(input('Digite um número entre 0 e 20: '))
    while usuario < 0 or usuario > 20:
        print('Número incorreto')
        usuario = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros_tupla[usuario]}')