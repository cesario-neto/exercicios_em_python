"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
numeros = input('Digite os números que voce deseja saber a média separando-os por vírgula(,): ')
numeros = numeros.split(',')

qnt = len(numeros)
soma = 0
for x in numeros:
    soma += float(x)

print(f'A média dos números que você digitou é {soma/qnt}')
