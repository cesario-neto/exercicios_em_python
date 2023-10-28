"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

try:
    numero = int(input('Digite um número inteiro e direi se ele é primo ou não: '))
    
    count = 0
    for x in range(1, (numero + 1)):
        if numero % x == 0:
            count += 1
            
    if count <= 2:
        print('O número digitado é primo.')
    else:
        print('O número digitado não é primo.')
    
except:
    print('Digite apenas números inteiros.')