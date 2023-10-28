"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""
numero = input('Digite um número: ')

try:
    numero = int(numero)
    
    if numero % 2 == 0:
        print('Esse número é PAR')
    else:
        print('Esse número é ÍMPAR')
    
except:
    print('Digite apenas números')