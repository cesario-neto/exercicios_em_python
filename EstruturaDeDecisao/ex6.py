"""
Faça um Programa que leia três números e mostre o maior deles.
"""
numero = input('Digite 3 números separando com , : ')
numero = numero.split(',')
lista_com_numeros = [int(valor) for valor in numero]
lista_com_numeros = sorted(lista_com_numeros)
print('O maior número que você digitou foi:', lista_com_numeros[-1])


# OU

# numero1 = float(input('Digite um número: '))
# numero2 = float(input('Digite outro número: '))
# numero3 = float(input('Digite outro número: '))

# maior = numero1
# if numero2 > numero1 and numero2 > numero3:
#     maior = numero2
# if numero3 > numero2 and numero3 > numero1:
#     maior = numero3

# print(maior)