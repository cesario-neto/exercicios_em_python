"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

numeros = input('Digite 10 números inteiros separando por vírgula(,): ')
numeros = numeros.split(',')

while len(numeros) < 10 or len(numeros) > 10:
    numeros = input('Digite 10 números inteiros separando por vírgula(,): ')
    numeros = numeros.split(',')

par = 0
impar = 0

for i in numeros:
    if float(i) % 2 == 0:
        par += 1
        print(f'{i} é PAR')
    else:
        impar += 1
        print(f'{i} é ÍMPAR')

print(f'\nTotal:\nPAR = {par}\nÍMPAR = {impar}')