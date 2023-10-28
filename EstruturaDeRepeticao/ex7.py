"""
Faça um programa que leia 5 números e informe o maior número.
"""

tentativas = 0
numero_temp = 0

while tentativas  < 5:
    num1 = float(input('Digite um número: '))
    
    if num1 > numero_temp:
        numero_temp = num1
    else:
        pass
    
    tentativas += 1
    
print(f'O maior número que você digitou foi {numero_temp}')