"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
while True:
    sexo = input('Digite M se for masculido ou F se for feminino: ')
    sexo = sexo.upper()
    if sexo == 'M':
        print('Você é do sexo masculino.')
        break
    elif sexo == 'F':
        print('Você é do sexo feminino.')
        break
    else:
        print('Sexo invalido...\nTente novamente.')