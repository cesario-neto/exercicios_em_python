"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""

numero = input('Digite um número: ')
numero = numero.replace(',', '.')

# if numero.find('.'):
#     print('É um número decimal')
# else:
#     print('É um número inteiro')

numero = float(numero)

if numero == round(numero):
    print('Número inteiro')
else:
    print('Número decimal')

# try:
#     numero = int(numero)
#     print('É um número inteiro')
    
# except ValueError:
#     print('É um número decimal')