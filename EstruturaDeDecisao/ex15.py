"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

num1 = input('Digite o valor de um lado do triangulo: ')
num2 = input('Digite o valor de outro lado do triangulo: ')
num3 =input('Digite o valor do último lado restante do triangulo: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    
    if num1 == num2 and num1 == num3 and num2 == num3:
        print('Esse é um Triângulo Equilátero')
    elif num1 == num2 and num1 != num3 or num2 == num3 and num2 != num1 or num3 == num1 and num3 != num2:
        print('Esse é um Triângulo Isósceles')
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print('Esse é um Triângulo Escaleno')
    
except:
    print('Digite apenas números')