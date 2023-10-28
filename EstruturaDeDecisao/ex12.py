"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_hora = input('Digite o valor ganho por hora: ')
horas = input('Digite a quantidade de horas trabalhada: ')
valor_hora = valor_hora.replace(',', '.')

try:
        valor_hora = float(valor_hora)
        horas = int(horas)
        
        salario_bruto = valor_hora * horas
        inss = salario_bruto * (10/100)
        fgts = salario_bruto * (11/100)
        
        ir_cinco_porcento = salario_bruto * (5/100)
        ir_dez_porcento = salario_bruto * (10/100)
        ir_vinte_porcento = salario_bruto * (20/100)

        if salario_bruto <= 900:
                print(f'Salário Bruto: ({valor_hora} * {horas}): R${salario_bruto}')
                print(f'(-) INSS ( 10%) : R${inss}')
                print(f'FGTS (11%) : R${fgts}')
                print(f'Total de descontos: R${inss}')
                print(f'Salário Líquido: R${salario_bruto - (inss)}')
                
        if salario_bruto <= 1500 and salario_bruto > 900:
                print(f'Salário Bruto: ({valor_hora} * {horas}): R${salario_bruto}')
                print(f'(-) IR (5%) : R%{ir_cinco_porcento}')
                print(f'(-) INSS ( 10%) : R${inss}')
                print(f'FGTS (11%) : R${fgts}')
                print(f'Total de descontos: R${inss + ir_cinco_porcento}')
                print(f'Salário Líquido: R${salario_bruto - (inss + ir_cinco_porcento)}')
                
        if salario_bruto > 1500 and salario_bruto <= 2500:
                print(f'Salário Bruto: ({valor_hora} * {horas}): R${salario_bruto}')
                print(f'(-) IR (10%) : R%{ir_dez_porcento}')
                print(f'(-) INSS ( 10%) : R${inss}')
                print(f'FGTS (11%) : R${fgts}')
                print(f'Total de descontos: R${inss + ir_dez_porcento}')
                print(f'Salário Líquido: R${salario_bruto - (inss + ir_dez_porcento)}')
        if salario_bruto > 2500: 
                print(f'Salário Bruto: ({valor_hora} * {horas}): R${salario_bruto}')
                print(f'(-) IR (20%) : R%{ir_vinte_porcento}')
                print(f'(-) INSS ( 10%) : R${inss}')
                print(f'FGTS (11%) : R${fgts}')
                print(f'Total de descontos: R${inss + ir_vinte_porcento}')
                print(f'Salário Líquido: R${salario_bruto - (inss + ir_vinte_porcento)}')
                
                
except ValueError as error:
        print('Digite apenas números.')