"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""

print('a. o produto do dobro do primeiro com metade do segundo.\nb. a soma do triplo do primeiro com o terceiro.\nc. o terceiro elevado ao cubo.')

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n_real = float(input('Digite um número real: '))

print(f'a = {((n1 * 2) + (n2 / 2))}')
print(f'b = {(n1 * 3) + n_real}')
print(f'c = {n_real ** 3}')
