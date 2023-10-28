"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""
try:
    numero = int(input('Digite um número inteiro e direi se ele é primo ou não: '))
    divisiveis = []
    
    count = 0
    for x in range(1, (numero + 1)):
        if numero % x == 0:
            count += 1
            divisiveis.append(x)
            
    divisiveis = str(divisiveis)
    divisiveis = divisiveis.replace('[', '')
    divisiveis = divisiveis.replace(']', '')
    if count <= 2:
        print('O número digitado é primo.')
    else:
        print('O número digitado não é primo.')
        print(f'{numero} é divisivel por: {divisiveis}')
    
except ValueError:
    print('Digite apenas números inteiros.')