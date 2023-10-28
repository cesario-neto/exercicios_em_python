"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""

genero = input('Digite se você é "h" (homen) ou "m" (mulher)? ')
genero = genero.lower()
altura = altura = input('Agora digite sua altura: ')
altura = altura.replace(',' , '.')
altura = float(altura)

if genero == 'h':
    print(f'Seu peso ideal será {(72.7*altura) - 58:.3f}Kg')
elif genero == 'm':
    print(f'Seu peso ideal será {(62.1*altura) - 44.7:.3f}Kg')
else:
    print('Responda a primeira pergunta com "h" ou "m".')
