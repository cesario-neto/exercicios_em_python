"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

# while True:
#     try:
#         numero = input('Digite um número entre 0 e 10: ')
#         numero = int(numero)
#         if numero >= 0 and numero <= 10:
#             print('Valido.'),
#             break
#         else:
#             print('inválido')
        
        
#     except: 
#         print('Digite apenas números')

numero = float(input('Digite um número entre 0 e 10: '))

while (numero<0) or (numero>10):
    print('inválido')
    numero = float(input('Digite um número entre 0 e 10: '))
    
else:
    print('válido')
    