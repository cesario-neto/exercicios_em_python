"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
soma = 0

if num1 > num2:
    print('O primeiro número não pode ser maior que o segundo número.')
else:
    for i in range(num1, (num2 + 1)):
        print(i, end=' ')
        soma = soma + i

print(f'\nA soma dos números é {soma}')