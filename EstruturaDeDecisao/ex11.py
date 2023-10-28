"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
def converte_float(valor):
    valor = valor.replace(',' ,'.')
    valor = float(valor)
    return valor

def converte_real(valor):
    return f'R${valor:.2f}'.replace('.' ,',')

salario_atual = converte_float(input('Digite seu salário: '))

if salario_atual <= 280:
    reajuste = 20
    aumento = salario_atual * reajuste/100
    salario_posterior = salario_atual + aumento
    print(f'Seu salário é de {converte_real(salario_atual)} e com aumento de {reajuste}% ({converte_real(aumento)}) passará a ser {converte_real(salario_posterior)}')
if salario_atual > 280 and salario_atual <= 700:
    reajuste = 15
    aumento = salario_atual * reajuste/100
    salario_posterior = salario_atual + aumento
    print(f'Seu salário é de {converte_real(salario_atual)} e com aumento de {reajuste}% ({converte_real(aumento)}) passará a ser {converte_real(salario_posterior)}')
if salario_atual > 700 and salario_atual <= 1500:
    reajuste = 10
    aumento = salario_atual * reajuste/100
    salario_posterior = salario_atual + aumento
    print(f'Seu salário é de {converte_real(salario_atual)} e com aumento de {reajuste}% ({converte_real(aumento)}) passará a ser {converte_real(salario_posterior)}')
if salario_atual > 1500:
    reajuste = 5
    aumento = salario_atual * reajuste/100
    salario_posterior = salario_atual + aumento
    print(f'Seu salário é de {converte_real(salario_atual)} e com aumento de {reajuste}% ({converte_real(aumento)}) passará a ser {converte_real(salario_posterior)}')
