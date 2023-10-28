"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

saque = input('Digite o valor que para saque (de R$10 à R$600): ')

if int(saque) < 10 or int(saque) > 600:
    print('Digite um valor entre 10 a 600.')
else:
    cem = int(saque)//100
    saque = int(saque) % 100

    cinquenta = int(saque) // 50
    saque = int(saque) % 50

    dez = int(saque) // 10
    saque = int(saque) % 10

    cinco = int(saque) // 5
    saque = int(saque) % 5

    um = int(saque) // 1
    saque = int(saque) % 1

    print(f'{cem} notas de R$100')
    print(f'{cinquenta} notas de R%50')
    print(f'{dez} notas de R$10')
    print(f'{cinco} notas de R$5')
    print(f'{um} notas de R$1')