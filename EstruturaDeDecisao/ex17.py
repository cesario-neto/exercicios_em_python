"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""

try:
    ano = input('Digite um ano na qual queira saber se foi bissexto ou não: ')
    ano = int(ano)
    
    if (ano%4) == 0:
        if (ano%100) == 0:
            if (ano%400) == 0:
                print(f'{ano} é um ano bissexto')
            else:
                print(f'{ano} não é um ano bissexto')
        else:
            print(f'{ano} é um ano bissexto')
    else:
        print(f'{ano} não é um ano bissexto')
        
    
except:
    print('digite apenas números inteiros')