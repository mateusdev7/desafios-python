frase = str(input('Digite uma frase\n>').strip().upper())
print(f'Na sua frase a letra A aparece {frase.count("A")} vezes')
print(f'A letra A na sua frase aparece pela primeira vez na posição {frase.find("A")+1}')
print(f'A letra A na sua frase apareceu pela última vez na posição {frase.rfind("A")+1} ')
