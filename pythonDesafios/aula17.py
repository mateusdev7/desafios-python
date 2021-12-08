# Inicialização 
# x = []
#  ou
# x = list()


# x.append(10) -> Adiciona o elemento 10 na ultima posição
# x.pop() -> Retira o último elemento(ver pilhas/E.D)
# x.insert(2, "oi") -> Insere na posição 2 o elemento "Oi"
# x.remove("oi") -> Remove o item "Oi" da lista.
# del x(3) -> Remove pelo indíce
# x.sort() -> Ordena a lista

x = []
for c in range(4):
    num = int(input('Digite um valor: '))
    x.append(num)
    if num == 2:
        x.remove(2)
        print('Foi removido o valor 2 da lista')
    x.sort()
print(x)
print('Nós temos os valores: ')
for v in x:
    print(f'{v}')
for c, v in enumerate(x):
    print(f'Na posição {c} encontei o valor {v}!')
print("Fim do código")