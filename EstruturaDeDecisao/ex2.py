"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
while True:
    numero = float(input('Digite um número: '))

    if numero < 0:
        print('Esse número é negativo.')
    else:
        print('Esse número é positivo.')