"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

numeros = input('Digite 2 números separando por vírgula (obs: se for número decimal, indicar com ponto "."): ')
lista = numeros.split(',')
lista_numeros = []

if len(lista_numeros) == 2:
    for num in lista:
        lista_numeros.append(float(num))
        
    print('O que você deseja que eu faça?')
    print('Identificar se os números são PAR ou ÍMPAR? digite 1')
    print('Identificar se os números são positivo ou negativo? digite 2')
    print('Identificar se os números são inteiro ou decimais? digite 3')

    escolha = int(input('O que você quer fazer? (digite 1, 2 ou 3): '))

    if escolha == 1:
        if lista_numeros[0] % 2 == 0:
            print(f'{lista_numeros[0]} é PAR')
        else:
            print(f'{lista_numeros[0]} é ÍMPAR')
            
        if lista_numeros[1] % 2 == 0:
            print(f'{lista_numeros[1]} é PAR')
        else:
            print(f'{lista_numeros[1]} é ÍMPAR')

    if escolha == 2:
        if lista_numeros[0] < 0:
            print(f'{lista_numeros[0]} é negativo')
        elif lista_numeros[0] > 0:
            print(f'{lista_numeros[0]} é positivo')
            
        if lista_numeros[1] < 0:
            print(f'{lista_numeros[1]} é negativo')
        elif lista_numeros[1] > 0:
            print(f'{lista_numeros[1]} é positivo')
            
    if escolha == 3:
        if round(lista_numeros[0]) == lista_numeros[0]:
            print(f'{lista_numeros[0]:.0f} é um número inteiro')
        else:
            print(f'{lista_numeros[0]} é um número decimal')
            
        if round(lista_numeros[1]) == lista_numeros[1]:
            print(f'{lista_numeros[1]:.0f} é um número inteiro')
        else:
            print(f'{lista_numeros[1]} é um número decimal')
            
    if escolha != 1 or escolha != 2 or escolha != 3:
        print('Escolha entre 1, 2 e 3')
else:
    print('Precisa-se digitar apenas 2 números')