"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
numero = input('Digite 3 números separando com , : ')
numero = numero.split(',')
lista_com_numeros = [int(valor) for valor in numero]
lista_com_numeros = sorted(lista_com_numeros)
print('O maior número que você digitou foi:', lista_com_numeros[-1])
print('O menor número que você digitou foi:', lista_com_numeros[0])

# OU

# num1 = float(input('Digite um número: '))
# num2 = float(input('Digite outro número: '))
# num3 = float(input('Digite outro número: '))

# maior = num1
# if num2 > num1 and num2 > num3:
#     maior = num2
# if num3 > num1 and num3 > num2:
#     maior = num3

# menor = num1
# if num2 < num1 and num2 < num3:
#     menor = num2
# if num3 < num1 and num3 < num2:
#     menor = num3

# print('Esse é o maior número que você digitou:', maior)
# print('Esse é o menor número que você digitou:', menor)
