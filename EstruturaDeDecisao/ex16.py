"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math

try:
    a = input('Digite o valor de a: ')
    a = int(a)
    if a == 0:
        print('A equação não será de 2° grau')
    else:
        b = input('Digite o valor de b: ')
        b = int(b)
        c = input('Digite o valor de c: ')
        c = int(c)

        x = (b**2) - (4 * a * c)
        x = x ** 0.5
        
        if x < 0:
            print('A equação não possui raizes reais')
        else:
            if x == 0:
                y_um = (-b + x) / (2 * a)
                print(f'A raíz é {y_um:.2f}')
            else:
                y_um = (-b + x) / (2 * a)
                y_dois = (-b - x) / (2 * a)
                print(f'A raíz y1 é {y_um}')
                print(f'A raíz y2 é {y_dois}')
                
except:
    print('Digite apenas números')

