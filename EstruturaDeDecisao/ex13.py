"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

dia = input('Digite um número de 1 a 7: ')

try:
    dia = int(dia)
    
    if dia >= 1 and dia <= 7:
        if dia == 1:
            print('O dia correpondente ao número é Domingo')
        if dia == 2:
            print('O dia correpondente ao número é Segunda-feira')
        if dia == 3:
            print('O dia correpondente ao número é Terça-feira')
        if dia == 4:
            print('O dia correpondente ao número é Quarta-feira')
        if dia == 5:
            print('O dia correpondente ao número é Quinta-feira')
        if dia == 6:
            print('O dia correpondente ao número é Sexta-feira')
        if dia == 7:
            print('O dia correpondente ao número é Sabado')
    else:
        print('digite um número entre 1 a 7')
    
except ValueError:
    print('Digite apenas números')