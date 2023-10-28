"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

ganho_por_hora = float(input('Digite quando ganha por hora: '))
horas_trabalhada_mes = int(input('Quantas horas trabalhada no mês: '))
salario_do_mes = ganho_por_hora * horas_trabalhada_mes
salario_liquido = salario_do_mes - ((salario_do_mes * 0.11) + (salario_do_mes * 0.08) + (salario_do_mes * 0.05))

print(f'Nesse mês você trabalhou {horas_trabalhada_mes}h ganhando R${ganho_por_hora} por hora.')
print(f'R${salario_do_mes:.2f} é o salário Bruto.')
print(f'R${salario_do_mes * 0.08:.2f} será descontado para o INSS(8%).')
print(f'R${salario_do_mes * 0.05:.2f} será descontado para o sindicato(5%).')
print(f'R${salario_do_mes * 0.11:.2f} será descontado do IR(11%).')
print(f'R${salario_liquido:.2f} será o valor líquido após os descontos.')
