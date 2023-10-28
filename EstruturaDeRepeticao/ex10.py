"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 < num2:
    print('O primeiro número não pode ser maior que o segundo número.')
else:
    for i in range(num1, (num2 + 1)):
        print(i, end=' ')