"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

ganho_por_hora = float(input('Digite quando ganha por hora: '))
horas_trabalhada_mes = int(input('Quantas horas trabalhada no mês: '))

print(f'Você trabalhou {horas_trabalhada_mes}h no mês recebendo R${ganho_por_hora:.2f} por hora, no total foram R${ganho_por_hora * horas_trabalhada_mes:.2f} ganho no mês.')