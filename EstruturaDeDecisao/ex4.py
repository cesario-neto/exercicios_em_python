"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
while True:
    letra = input('Digite uma letra ')
    letra = letra.upper()

    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print('A letra que você digitou é uma vogal.')
    else:
        print('A letra que você digitou é uma consoante.')


