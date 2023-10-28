"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
numeros = input('Digite as idades separando por vírgula(,): ')
numeros = numeros.split(',')

qnt = len(numeros)
soma = 0
for x in numeros:
    soma += float(x)

if (soma/qnt) > 0 and (soma/qnt) <= 25:
    print(f'A turma é jovem!')
if (soma/qnt) >= 26 and (soma/qnt) <= 60:
    print(f'A turma é adulta!')
if (soma/qnt) > 60:
    print(f'A turma é idosa!')

print(f'A média dos números que você digitou é {soma/qnt}')