"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = input('Digite um número abaixo de 1000: ')

if len(num) == 3:
    if int(num[0]) == 1 or int(num[0]) == 0:
        centena = 'centena'
    else:
        centena = 'centenas'
    
    if int(num[1]) == 1 or int(num[1]) == 0:
        dezena = 'dezena'
    else:
        dezena = 'dezenas'
    
    if int(num[2]) == 1 or int(num[2]) == 0:
        unidade = 'unidade'
    else:
        unidade = 'unidades'
        
    print(f'{num[0]} {centena}, {num[1]} {dezena} e {num[2]} {unidade}.')

if len(num) == 2:
    if int(num[0]) == 1 or int(num[0]) == 0:
        dezena = 'dezena'
    else:
        dezena = 'dezenas'
    
    if int(num[1]) == 1 or int(num[1]) == 0:
        unidade = 'unidade'
    else:
        unidade = 'unidades'
    
    print(f'{num[0]} {dezena} e {num[1]} {unidade}')
    
if len(num) == 1:
    if int(num[0]) == 1 or int(num[0]) == 0:
        unidade = 'unidade'
    else:
        unidade = 'unidades'
    
    print(f'{num} {unidade}')

if len(num) > 3:
    print('Não temo suporte para números maiores que 3 digitos')