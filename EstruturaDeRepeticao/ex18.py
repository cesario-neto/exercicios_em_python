"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

lista = []

while True:
    num_digitado = input('Digite um número inteiro ou (p) para parar: ')
    num_digitado = num_digitado.lower()
    if num_digitado == 'p':
        break
    try:
        num_digitado_temp = int(num_digitado)
        lista.append(num_digitado)
    except:
        print('digite apenas números inteiros ou digite p para parar.')
    
nova_lista = [int(x) for x in lista]
nova_lista.sort()

print(f'\nO Menor número que você digitou é {nova_lista[0]:.0f}\nO maior número digitado é {nova_lista[-1]:.0f}\nA soma de todos os números digitados é {sum(nova_lista):.0f}')