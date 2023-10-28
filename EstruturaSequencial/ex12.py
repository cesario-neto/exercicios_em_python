"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = input('Digite sua altura: ')
altura = altura.replace(',' , '.')
altura = float(altura)

print(f'Seu peso ideal será {(72.7*altura) - 58:.3f}Kg')